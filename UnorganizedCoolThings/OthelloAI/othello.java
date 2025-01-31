/*
Name: Christian Hall
Date: 11/11/2024
Description: Working Othello game + Minimax algorithm with alpha beta pruning! (significantly easier than neural nets)
*/

import java.util.Scanner;

public class othello{

    static boolean debug = true;
    static boolean pruning = true;

    public static int[][] gameBoard = initBoard();
    public static int fullDepth = 8;
    public static boolean blackAI;
    public static int numStatesExamined = 0;

    public static void main(String[] args){
        // Initialize the board which is an 8x8 int[][] with all 0's aside from 4 locations

        // show the initial board state
        printBoard(gameBoard);


        // init all variables that are needed inside the game
        boolean isGameOver = false;
        int turn = 1;
        Scanner input = new Scanner(System.in);
        int[] coords = new int[2];
        boolean blackAI;

        // we determine which thing color the AI will be
        if(Math.round(Math.random()) == 1){ //
            blackAI = true;
        }
        else{
            blackAI = false;
        }

        // start the game
        while(!isGameOver) {
            // when its an odd turn (turn 1 is the start) it is blacks turn. Black is represented as a -1 on the board
            while(turn % 2 == 1) {
                System.out.println("Debug - " + debug + "\t Pruning - " + pruning + "\n");
                // if black is not the AI that means black's the player so do player stuff
                if(!blackAI) {
                    System.out.println("Black (-1): Please enter a legal coordinant move or Command");
                    coords = interpret(input.nextLine());
                    // Use interpret function to run commands and get a coord for the next move
                    if (isLegalMove(gameBoard, turn, coords[0], coords[1])) {
                        makeLegalMove(gameBoard, turn, coords[0], coords[1]);
                        turn++;
                    }
                }
                // if Black is the ai then call the miniMax function and count the number of times it gets recursively
                // called
                else{
                    miniMax(gameBoard, fullDepth, Integer.MIN_VALUE, Integer.MAX_VALUE,true, turn);
                    if(debug){
                        System.out.println("Number of times MiniMax was called: " + numStatesExamined);
                    }
                    numStatesExamined = 0;
                    turn++;
                }
            }

            // print the move after its made.
            printBoard(gameBoard);

            // if there are no moves available then break out of the game loop
            if(numLegalMoves(gameBoard, turn) == 0){
                break;
            }

            // Whites turn (1)
            while(turn % 2 == 0) {
                // if black is the AI then white is the Human player
                if(blackAI) {
                    System.out.println("Debug - " + debug + "\t Pruning - " + pruning + "\n");

                    // use interpret function to run commands and get coords
                    System.out.println("White (1), Please enter a Coordinant move or command");
                    coords = interpret(input.nextLine());
                    // make move
                    if (isLegalMove(gameBoard, turn, coords[0], coords[1])) {
                        makeLegalMove(gameBoard, turn, coords[0], coords[1]);
                        turn++;
                    }
                }
                // if the AI is white then call the miniMax function and count the number of times it recursively calls
                else{
                    miniMax(gameBoard, fullDepth, Integer.MIN_VALUE, Integer.MAX_VALUE,true, turn);
                    if(debug){
                        System.out.println("Number of times MiniMax was called: " + numStatesExamined);
                    }
                    numStatesExamined = 0;
                    turn++;
                }
            }

            // print the board after white moves
            printBoard(gameBoard);

            // if there are no legal moves left on the board break out of the game loop
            if(numLegalMoves(gameBoard, turn) == 0){
                break;
            }
        }

        // out of the game loop. Call the winner function to determine who wins the game
        System.out.println(winner(gameBoard));
    }

    // this funnction takes in a string and outputs an int array... the output is an int[]
    // certain commands do certain things, but its mostly used to determine the coords used on the next move
    public static int[] interpret(String input){
        int[] val = {-2, -2};
        if(input.equalsIgnoreCase("help")){
            // command help prints all commands and things you can do
            System.out.println("--- Commands ---\n[debug]\tToggles Debug mode on and off\n[alphabeta]\tToggels alpha beta pruning on and off");
            System.out.println("[quit]\t exit the program\n\n---Entering a move---");
            System.out.println("Moves are entered in the format \"e3\" or \"53\" based on the coordinant system shown on the board");
            System.out.println("if you enter a move that is illegal the game will not accept that move and force you to enter another until you enter a move that is legal");
            return val;
        }
        // command quit exits the program
        else if(input.equalsIgnoreCase("quit")){
            System.exit(0);
            return val;
        }
        // command debug changes the debug variables state to the opposite current state
        else if(input.equalsIgnoreCase("debug")){
            debug = !debug;
            return val;
        }
        // command alphabeta changes the pruning variables state to the opposite state
        else if(input.equalsIgnoreCase("alphabeta")){
            pruning = !pruning;
            return val;
        }
        // if it is no recognized command then check to see if the input is only 2 characters.
        else if(input.length() == 2){
            // if 2 characters then turn return the int[] holding the proper coords
            if(Character.isAlphabetic(input.charAt(0)) && Character.isDigit(input.charAt(1))){
                char alphaVal = Character.toLowerCase(input.charAt(0));
                val[0] = ((alphaVal - 'a'));
                val[1] = (input.charAt(1) - '0') - 1;
            }
            else if(Character.isDigit(input.charAt(0)) && Character.isDigit(input.charAt(1))){
                val[0] = (input.charAt(0) - '0') - 1;
                val[1] = (input.charAt(1) - '0') - 1;
            }
            return val;
        }
        // if nothing is recognized return a value that forces the player to choose again
        else{
            return val;
        }
    }

    // is legal move checks in all 8 directions to see if there is a vector that meets the requirements to...
    // place a number there. This uses the check direction function
    public static boolean isLegalMove(int[][] board, int turn, int xCoord, int yCoord) {
        for(int i = -1; i <= 1; i++){
            for(int j = -1; j <= 1; j++){
                 if(checkDirection(board, i, j, xCoord, yCoord, turn)){
                     return true;
                 }
            }
        }
        return false;
    }

    // uses the checkdirection function to test to see if the move is legal then if it is, places either a 1 or -1 on
    // the xCoord and yCoord defined by the perameters passed into the function
    public static int[][] makeLegalMove(int[][] board, int turn, int xCoord, int yCoord){
        boolean isLegal = false;
        for(int i = -1; i <= 1; i++){
            for(int j = -1; j <= 1; j++){
                if(checkDirection(board, i, j, xCoord, yCoord, turn)){
                    isLegal = true;
                    if(turn % 2 == 1){
                        int k = 1;
                        while(board[yCoord + (i * k)][xCoord + (j * k)] == 1){
                            board[yCoord + (i * k)][xCoord + (j * k)] = -1;
                            k++;
                        }
                    }
                    else{
                        int k = 1;
                        while(board[yCoord + (i * k)][xCoord + (j * k)] == -1){
                            board[yCoord + (i * k)][xCoord + (j * k)] = 1;
                            k++;
                        }
                    }
                }
            }
        }
        // using turn to determine if black or white piece should go down
        if(isLegal){
            if(turn % 2 == 1) {
                board[yCoord][xCoord] = -1;
            }
            else{
                board[yCoord][xCoord] = 1;
            }
        }
        return board;
    }

    // Look in one direction see if that specific direction meets the requirements to have a tile placed on it.
    // it uses the turn to determine if its blacks piece or whites piece that should be placed.
    public static boolean checkDirection(int[][] board, int yDir, int xDir, int xCoord, int yCoord, int turn){
        try {
            int i = yCoord;
            int j = xCoord;
            if(board[yCoord][xCoord] == 0) {
                boolean possibleFlank = false;
                while (true) {
                    i += yDir;
                    j += xDir;
                    if (turn % 2 == 1) {
                        if (board[i][j] == 1) {
                            possibleFlank = true;
                        } else if (board[i][j] == -1 && possibleFlank) {
                            return true;
                        } else {
                            return false;
                        }
                    } else {
                        if (board[i][j] == -1) {
                            possibleFlank = true;
                        } else if (board[i][j] == 1 && possibleFlank) {
                            return true;
                        } else {
                            return false;
                        }
                    }
                }
            }
            return false;
        }
        // if at index 0 or 7 on either side and it tries to go to -1 or 8 respectively then this will throw an index...
        // out of bounds error. It is impossible to place anything outside the board so return false.
        catch(IndexOutOfBoundsException e){
            return false;
        }
    }

    // initialize the 2d array which will be used to hold the info that the game is held
    public static int[][] initBoard(){
        int[][] board = {
                {0,0,0,0,0,0,0,0},
                {0,0,0,0,0,0,0,0},
                {0,0,0,0,0,0,0,0},
                {0,0,0,1,-1,0,0,0},
                {0,0,0,-1,1,0,0,0},
                {0,0,0,0,0,0,0,0},
                {0,0,0,0,0,0,0,0},
                {0,0,0,0,0,0,0,0}
        };
        return board;
    }

    // formats the borad in a human readable way with a coordinant system to allow the player to read locations easier
    public static void printBoard(int[][] board){
        System.out.println("\t[1/A]\t[2/B]\t[3/C]\t[4/D]\t[5/E]\t[6/F]\t[7/G]\t[8/H]");
        for(int i = 0; i < board.length; i++){
            System.out.print("[" + (i+1) + "]\t");
            for(int j = 0; j < board[i].length; j++){
                System.out.print(board[i][j] + "\t");
            }
            System.out.println("\n\n");
        }
    }

    // check every position on the board and count how many are legal
    public static int numLegalMoves(int[][] board, int turn){
        int count = 0;
        for(int i = 0; i < board.length; i++){
            for(int j = 0; j < board[i].length; j++){
                directionalLoop: for(int k = -1; k <= 1; k++){
                    for(int l = -1; l <=1; l++){
                        if(checkDirection(board, k, l, i, j, turn)){
                            count++;
                            break directionalLoop;
                        }
                    }
                }
            }
        }
        return count;
    }

    // Call when the game is over: When this is called it will return the player with the most chips
    public static int winner(int[][] board){
        int black = 0;
        int white = 0;
        for(int i = 0; i < board.length; i++){
            for(int j = 0; j < board[i].length; j++){
                if(board[i][j] == -1){
                    black++;
                }
                else if(board[i][j] == 1){
                    white++;
                }
            }
        }
        if(black > white){
            return -1;
        }
        else{
            return 1;
        }
    }

    // Takes the board state and calls numLegalMoves to find how many legal moves there are. after finding the number...
    // of legal moves, you iterate through the board to get the locations. This returns a 2d int array where the ...
    // the number of arrays is the number of legal moves and in each array is a coord of a legal move
    public static int[][] getLegalMoves(int[][] board, int turn){
        int[][] possibleMoves = new int[numLegalMoves(board, turn)][2];
        int count = 0;
        for(int i = 0; i < board.length; i++){
            for(int j = 0; j < board[i].length; j++){
                if(isLegalMove(board, turn, j, i)){
                    possibleMoves[count][0] = j;
                    possibleMoves[count][1] = i;
                    count++;
                }
            }
        }
        return possibleMoves;
    }

    // takes in a board, returns the same board as a 2d Int array
    public static int[][] copyBoard(int[][] board){
        int[][] copy = new int[board.length][board[0].length];
        for(int i = 0; i < board.length; i++){
            for(int j = 0; j < board[i].length; j++){
                copy[i][j] = board[i][j];
            }
        }
        return copy;
    }

    // miniMax with alphaBeta pruning. Takes in board, the depth you want, whether youre maximizing or minimizing and...
    // what turn it is. This function recursively calls itself depth times for each possible move state on each board...
    // this uses a heuristic function based on mobility (mainly becuase it was easy to impliment) the more legal ...
    // moves you have the better. If you see a way to force a win, you take that instead. Since this is complicated...
    // comments will be dispersed throughout the function.
    public static int miniMax(int[][] board, int depth, int alpha, int beta, boolean isMaximizing, int turn) {
        // increase the static variable here to count how many times this function was called recursively.
        numStatesExamined++;
        // if we get to a depth of 0 or someone wins, calculate the heuristic
        if(depth == 0 || numLegalMoves(board, turn) == 0){
            if(numLegalMoves(board, turn) == 0){
                if((winner(board) == 1 && blackAI == false) || winner(board) == -1 && blackAI == true){
                    return Integer.MAX_VALUE;
                }
                else{
                    return Integer.MIN_VALUE;
                }
            }
            return numLegalMoves(board, turn) - numLegalMoves(board, turn + 1);
        }
        // if its the AI's turn, it goes here to maximize the function.
        if(isMaximizing){
            // start out with a max eval of -2 billion because it doesn't get lower than that.
            int maxEval = Integer.MIN_VALUE;
            // loop through each legal move
            for(int i = 0; i < numLegalMoves(board, turn); i++){
                // make a copy of the board becasue updating gameBoard here causes *ISSUES* and get all legal moves
                int[][] copy = copyBoard(board);
                int[][] legalMoves = getLegalMoves(copy, turn);

                // make one of the legal moves then call the miniMax algorithm for the players turn.
                makeLegalMove(copy, turn, legalMoves[i][0], legalMoves[i][1]);
                int eval = miniMax(copy, depth - 1, alpha, beta,false, turn + 1);

                // after getting the value "eval" from minimax maximize it with the current value of
                maxEval = Math.max(maxEval, eval);
                if(pruning){
                    alpha = Math.max(alpha, eval);
                    if(beta <= alpha){
                        break;
                    }
                }
                // DEBUG print out the max eval compared to the returned eval (this was because of an error i had)
                if(debug){
                    if(depth == fullDepth){
                        System.out.println(maxEval + ", " + eval);
                    }
                }

                // if you are at the top depth and you see a Max eval, then set the gameBoard = to the copy
                if(depth == fullDepth && eval == maxEval){
                    // DEBUG print out all the legal moves.
                    if(debug){
                        System.out.println("Placed at " + (legalMoves[i][0] + 1) + ", " + (legalMoves[i][1] + 1));
                    }
                    gameBoard = copy;
                }
            }
            // return the Max value
            return maxEval;
        }

        //Minimizer function
        else{
            // set the starting minimum value to the largest number we can, its all downhill from here.
            int minEval = Integer.MAX_VALUE;
            // loop through every child
            for(int i = 0; i < numLegalMoves(board, turn); i++){
                // copy board and store all legal moves
                int[][] copy = copyBoard(board);
                int[][] legalMoves = getLegalMoves(copy, turn);

                // make a legal move
                makeLegalMove(copy, turn, legalMoves[i][0], legalMoves[i][1]);
                // call minimax as a maximizer
                int eval = miniMax(copy, depth - 1, alpha, beta,true, turn + 1);
                // calculate the best move for the opponent, and prune what isn't needed
                minEval = Math.min(minEval, eval);
                if(pruning){
                    beta = Math.min(beta, eval);
                    if(beta <= alpha){
                        break;
                    }
                }
                // DEBUG print the current eval and min eval (because of that problem)
                if(debug){
                    if(depth == fullDepth){
                        System.out.println(minEval + ", " + eval);
                    }
                }
                // when you find a new minEval setGameboard = to copy
                if(depth == fullDepth && eval == minEval){
                    // DEBUG Print out the legal move that was made by the computer (it will choose the last best one)
                    if(debug) {
                        System.out.println("Placed at" + (legalMoves[i][0] + 1) + ", " + (legalMoves[i][1] + 1));
                    }
                    gameBoard = copy;
                }
            }
            // return minValue
            return minEval;
        }
    }
}