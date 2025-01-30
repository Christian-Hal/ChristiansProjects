/*
Name: Christian Hall
Date: Started 9/25/24 - Ended
Description:

 */
import java.io.File;
import java.io.FileNotFoundException;
import java.io.FileWriter;
import java.io.IOException;
import java.util.Arrays;
import java.util.Collections;
import java.util.List;
import java.util.Scanner;

public class neuralnet{

    // This is where we initialize all of the data that we can use to customize our network!
    // Any of these values must change depending on the network we want to run.
    public static int numLayers = 3;
    public static int numInputs = 784;
    public static int hiddenLayerInputs = 25;
    public static int numOutputs = 10;
    public static int miniBatchSize = 10;
    public static double learningRate = 3;
    public static int totalTrainingPoints = 60_000;
    public static int totalTestingPoints = 10_000;
    public static int[] LayerNodes = {numInputs, hiddenLayerInputs, numOutputs};

    public static void main(String[] args) throws FileNotFoundException {
        // this is the location of the raw data files that will be used in part 2
        String filePath = System.getProperty("user.dir") + "/data.csv";

        // I know that i will need a certain amount of matrixes to do math with. If i create a weight, bias, vector, and
        // gradients matrix for each layer, I know i will have enough
        Matrix[] weights = new Matrix[numLayers];
        Matrix[] biases = new Matrix[numLayers];
        Matrix[] vectors = new Matrix[numLayers];
        Matrix[] biasGrads = new Matrix[numLayers];
        Matrix[] weightGrads = new Matrix[numLayers];

        // network debug mode, shows raw values of nearly all data that is used in the network
        boolean debug = false;

        // If debug mode is on, this prints the number of layers, inputs and outputs in the network
        if(debug){
            System.out.println("Network Details!\nNumber of Layers \t" + numLayers);
            System.out.println("Number of inputs\t" + numInputs);
            System.out.println("Number of outputs\t" + numOutputs + "\n");
        }

        System.out.println("Initializing Data from CSV Files");

        // this for loop initializes the weights matrices based on the number of nodes in each Layer (all values to 0)
        for(int i = 0; i < numLayers - 1; i++){
            Matrix weight = new Matrix(LayerNodes[i+1], LayerNodes[i]);
            weights[i] = weight;
        }

        // this for loop initializes the biases matrices based on the number of nodes in each Layer (all values to 0)
        for(int i = 0; i < numLayers - 1; i++){
            Matrix bias = new Matrix(LayerNodes[i+1], 1);
            biases[i] = bias;
        }

        // this for loop initializes the nodes matrices with the proper dimensions (all values to 0)
        for(int i = 0; i < numLayers; i++){
            Matrix vector = new Matrix(LayerNodes[i], 1);
            vectors[i] = vector;
        }

        // this for loop initializes the Bias gradients with the proper dimensions (all values to 0)
        for(int i = 0; i < numLayers - 1; i++){
            Matrix biasGrad = new Matrix(LayerNodes[i+1], 1);
            biasGrads[i] = biasGrad;
        }

        // this loop initializes the weight gradients with the proper dimensions (all values to 0)
        for(int i = 0; i < numLayers - 1; i++){
            Matrix weightGrad = new Matrix(LayerNodes[i+1], LayerNodes[i]);
            weightGrads[i] = weightGrad;
        }

        Scanner vScanner = new Scanner(new File(filePath));
        double[][] vScanVals = new double[totalTrainingPoints][numInputs + 1];
        for(int i = 0; i < totalTrainingPoints; i++){
            String[] str = (vScanner.nextLine().split("[,]"));
            for (int j = 0; j < str.length; j++) {
                vScanVals[i][j] = Double.valueOf(str[j]);
            }
        }
        vScanner.close();

        Scanner v2Scanner = new Scanner(new File(System.getProperty("user.dir") + "/test.csv"));
        double[][] testingSet = new double[totalTestingPoints][numInputs + 1];
        for(int i = 0; i < totalTestingPoints; i++){
            String[] str = v2Scanner.nextLine().split("[,]");
            for(int j = 0; j < str.length; j++){
                testingSet[i][j] = Double.valueOf(str[j]);
            }
        }

        Layer[] network = new Layer[numLayers];
        for (int i = 0; i < numLayers; i++) {
            network[i] = new Layer(weights[i], vectors[i], biases[i], biasGrads[i], weightGrads[i]);
        }

        // initialize the network, this creates an array of layers that can be used to access different parts of the
        // network
        int choice = initProgram();
        while(true) {

            double error = 0;
            // test print
            if (debug) {
                for (int i = 0; i < weights.length; i++) {
                    System.out.println("Weights: \n" + weights[i]);
                    System.out.println("Vectors: \n" + vectors[i]);
                    System.out.println("Biases: \n" + biases[i]);
                }
            }


            if (choice == 0) {
                System.exit(0);
            }

            if (choice == 1) {
                for (int i = 0; i < weights.length - 1; i++) {
                    ;
                    for (int j = 0; j < network[i].weights.numColumn; j++) {
                        for (int k = 0; k < network[i].weights.numRow; k++) {
                            network[i].weights.setMatData(j, k, (Math.random() * 2) - 1);
                        }
                    }
                }

                for (int i = 0; i < biases.length - 1; i++) {
                    for (int j = 0; j < network[i].bias.numColumn; j++) {
                        network[i].bias.setMatData(j, 0, (Math.random() * 2) - 1);
                    }
                }


                // Initialize all the variables that i will need later on after doing the forward pass and backpropogation
                double epoch = 0;
                int vecMax = 0;
                int numCorrect = 0;

                // This while loop is the start of the forward passes and backpropogation. It will repeat passes until it meets
                // either stated condition.
                while (error < 0 || epoch < 5) {
                    int one = 0, two = 0, three = 0, four = 0, five = 0, six = 0, seven = 0, eight = 0, nine = 0, zero = 0;
                    int zeroR = 0, oneR = 0, twoR = 0, threeR = 0, fourR = 0, fiveR = 0, sixR = 0, sevenR = 0, eightR = 0, nineR = 0;
                    // right here we will need to randomize the data set
                    // <INPUT THE RAND FUNCT HERE>
                    List<double[]> list = Arrays.asList(vScanVals);
                    Collections.shuffle(list);
                    list.toArray(vScanVals);


                    System.out.println("\nEpoch = " + epoch);

                    // This is the start of the forward pass loops. Each weight and bias gets updated totalTrainingPoints/minibatchSize
                    // times per Epoch. So we make a for loop that loops over the scanner values once but in groups of whatever
                    // the minibatch is set to. I then update the weights and biases after looping through one full mini-batch
                    for (int i = 0; i < totalTrainingPoints; i += miniBatchSize) {

                        // This is where the magic happens This loops over every vector/activation layer in a minibatch, and
                        // then updates the values based on the backpropogation and gradient decent that was implimented in
                        // the same for loop
                        for (int j = 0; j < miniBatchSize; j++) {

                            // this saves the solution at index 0, we will need it to make a one hot vector later
                            int solution = Integer.valueOf((int) vScanVals[i + j][0]);
                            //System.out.println(solution);
                            // This for loop converts the String[] into doubles which get placed into activation layer 0
                            for (int k = 0; k < vScanVals[i + j].length - 1; k++) {
                                network[0].vector.setMatData(k, 0, Double.valueOf(vScanVals[i + j][k + 1]));
                            }
                            for(int k = 0; k < network[0].vector.numColumn; k++){
                                network[0].vector.setMatData(k,0, network[0].vector.getMatData(k,0) / 255);
                            }
                            // Using the already initialized weights and biases we calculate the activation layers in the
                            // next layer.
                            for (int k = 0; k < network.length - 1; k++) {
                                network[k + 1].vector = network[k].calculateNext();
                            }

                            // Longwinded explaination of the falseBias Matrix incoming... Later on in this for loop i update
                            // the bias gradient, to do this i add some number to the already existing bias called either oneHot
                            // or baisOut. I have to save these temporary variables for later because biasGradient is a sum, not
                            // the actual biasGradient of that layer. Thus i need to make a variable to save the bias gradient
                            // value of the last layer.
                            // [Note] i did not have this problem with the weight gradient because of my implimentation not
                            // needing to reference the last layers true weight gradient value.
                            Matrix falseBias = new Matrix(network[0].biasGradient.numColumn, network[0].biasGradient.numRow);

                            // This is the backpropogation function.
                            for (int k = network.length - 1; k > 0; k--) {
                                // if k is the network length - 1 then we are in the last layer of the network.
                                if (k == network.length - 1) {
                                    // Create the Matrices that will define the biasGradient and WeightGradient
                                    Matrix oneHot = new Matrix(vectors[k].numColumn, vectors[k].numRow);
                                    Matrix weightOut = new Matrix(network[k - 1].weightGradient.numColumn, network[k - 1].weightGradient.numRow);
                                    // set OneHot to a one hot matrix with the 1 on the solutions index. I have an add funciton
                                    // but no subtract, so making this = -1 does the same thing as subtraction.
                                    oneHot.setMatData(solution, 0, -1);

                                    // add the one hot to the activation layer in the last layer
                                    // this simulates (a_j - y_j)
                                    oneHot = oneHot.add(network[k].vector);

                                    // this for loop simulates the equation output = oneHot * a_j * (1 - a_j) where ...
                                    // a_j is always of the last layer. since output = the biasGradient, we add it to the
                                    // total bias gradient (we do the sum of the biasGradient for Gradient decent)
                                    for (int l = 0; l < oneHot.numColumn; l++) {
                                        oneHot.setMatData(l, 0, oneHot.getMatData(l, 0) * network[k].vector.getMatData(l, 0));
                                        oneHot.setMatData(l, 0, oneHot.getMatData(l, 0) * (1 - network[k].vector.getMatData(l, 0)));
                                        for (int m = 0; m < network[k - 1].weightGradient.numRow; m++) {
                                            weightOut.setMatData(l, m, network[k - 1].vector.getMatData(m, 0) * oneHot.getMatData(l, 0));
                                        }
                                    }

                                    // update falseBias so that it equals the current layers true, nonsummed bias gradient
                                    falseBias = oneHot;

                                    // update biasGradient to be the current bias gradient + the new bias gradient
                                    // update weightGradinet to be the current weightgradient
                                    network[k - 1].biasGradient = network[k - 1].biasGradient.add(oneHot);
                                    network[k - 1].weightGradient = network[k - 1].weightGradient.add(weightOut);

                                }

                                // we are in any layer aside from the last layer. (this of course changes the backpropogation
                                // ... equations we use)
                                else {
                                    // Initialize the biasOut Matrix and WeightOut Matrix. These will be used later to solve
                                    // ... backpropagation.
                                    Matrix biasOut = new Matrix(network[k].vector.numColumn, network[k].vector.numRow);
                                    Matrix weightOut = new Matrix(network[k - 1].weightGradient.numColumn, network[k - 1].weightGradient.numRow);

                                    // this for loop l solves the equation output = (weightSum * falseBias) * a_k * (1-a_k)
                                    for (int l = 0; l < biasOut.numColumn; l++) {

                                        // Grab the activation from the last layer and multiply it by 1 - itself
                                        double activationL = network[k].vector.getMatData(l, 0);
                                        activationL = (activationL * (1 - activationL));

                                        // init weightSum and loop through each weight and multiply it by the correct bias
                                        // ... This also equals (weightSum * falseBias)
                                        double weightSum = 0;
                                        for (int m = 0; m < network[k].weights.numColumn; m++) {
                                            weightSum += falseBias.getMatData(m, 0) * network[k].weights.getMatData(m, l);
                                        }

                                        // multiply (weight * falsebias) by (a_k * (1 - a_k)) to get the output
                                        biasOut.setMatData(l, 0, weightSum * activationL);

                                        // set each number in the output equal to weightOut so it can be accessed outside the
                                        // ... for loop
                                        for (int m = 0; m < network[k - 1].weightGradient.numRow; m++) {
                                            weightOut.setMatData(l, m, network[k - 1].vector.getMatData(m, 0) * biasOut.getMatData(l, 0));
                                        }
                                    }
                                    // reset falseBias so that it is the correct value for all future layers
                                    falseBias = biasOut;

                                    // Finally set the biasGradient and weight gradient to the correct values
                                    network[k - 1].biasGradient = network[k - 1].biasGradient.add(biasOut);
                                    network[k - 1].weightGradient = network[k - 1].weightGradient.add(weightOut);
                                }

                            }

                            // print the whole network.
                            if (debug) {
                                for (int k = 0; k < numLayers; k++) {
                                    System.out.println(network[k]);
                                }
                            }

                            // grab the index of the maximum activation value from the final layer of the network.
                            for (int k = 0; k < network[network.length - 1].vector.numColumn; k++) {
                                if (network[network.length - 1].vector.getMatData(k, 0) > network[network.length - 1].vector.getMatData(vecMax, 0)) {
                                    vecMax = k;
                                }
                            }
                            // prints to know we're getting things right... this prints the actual solution and the solution
                            // that our network was able to find.
                            // if they are equal it says its anwser is correct, otherwise, it says it was wrong
                            if (solution == vecMax) {
                                numCorrect++;
                            }
                            switch(vecMax){
                                case 1: one++; break;
                                case 2: two++; break;
                                case 3: three++; break;
                                case 4: four++; break;
                                case 5: five++; break;
                                case 6: six++; break;
                                case 7: seven++; break;
                                case 8: eight++; break;
                                case 9: nine++; break;
                                case 0: zero++; break;
                            }
                            switch(solution){
                                case 1: oneR++; break;
                                case 2: twoR++; break;
                                case 3: threeR++; break;
                                case 4: fourR++; break;
                                case 5: fiveR++; break;
                                case 6: sixR++; break;
                                case 7: sevenR++; break;
                                case 8: eightR++; break;
                                case 9: nineR++; break;
                                case 0: zeroR++; break;
                            }
                        }

                        // after running through the whole minibatch we need to update our weights and biases using our newly
                        // ... found bias gradients, after that, we set each biasGradient and
                        for (int j = 0; j < network.length - 1; j++) {
                            network[j].calculateNewWeights(learningRate, miniBatchSize);
                            network[j].calculateNewBiases(learningRate, miniBatchSize);
                            network[j].biasGradient = new Matrix(LayerNodes[j + 1], 1);
                            network[j].weightGradient = new Matrix(LayerNodes[j + 1], LayerNodes[j]);

                        }
                    }
                    // calculate the error, and print it
                    System.out.println((((double) numCorrect / totalTrainingPoints) * 100) + "%");
                    System.out.println("Accuracy = " + numCorrect + "/" + totalTrainingPoints);

                    System.out.println("1 = " + one + "/" + oneR + "\t2 = " + two + "/" + twoR + "\t3 = " + three + "/" + threeR + "\t4 = " + four + "/" + fourR + "\t5 = " + five + "/" + fiveR);
                    System.out.println("6 = " + six + "/" + sixR + "\t7 = " + seven + "/" + sevenR + "\t8 = " + eight + "/" + eightR + "\t9 = " + nine + "/" + nineR + "\t0 = " + zero + "/" + zeroR);


                    // increment the epoch and reset the number of correctly identified values.
                    epoch++;
                    numCorrect = 0;

                }
            }

            if (choice == 2) {
                // use the weights found in weights.csv and place them as the weights in the weight Matrix arrays
                Scanner wScanner = new Scanner(new File(System.getProperty("user.dir") + "/weights.csv"));
                for (int i = 0; i < weights.length - 1; i++) {
                    String[] wScanVals = wScanner.nextLine().split("[,]");
                    for(int j = 0; j < wScanVals.length; j++){
                        int col = j / (network[i].weights.numRow);
                        int row = j % (network[i].weights.numRow);
                        network[i].weights.setMatData(col, row, Double.valueOf(wScanVals[j]));
                    }
                }

                // to not waste space, we close the scanner.
                wScanner.close();

                // use the biases found in the biases.csv and place them in the bias Matrix arrays
                Scanner bScanner = new Scanner(new File(System.getProperty("user.dir") + "/biases.csv"));
                for (int i = 0; i < biases.length - 1; i++) {
                    String[] bScanVals = bScanner.nextLine().split("[,]");
                    for (int j = 0; j < network[i].bias.numColumn; j++) {
                        //Take the specific value found by scanner and input it into the proper bias Matrix
                        network[i].bias.setMatData(j, 0, Double.valueOf(bScanVals[j]));
                    }
                }
                // close the scanner to save space
                bScanner.close();
            }

            choice = contProgram();

            if (choice == 3 || choice == 4 || choice == 5 || choice == 6) {
                int numberOfInputs = totalTestingPoints;
                if(choice == 3){
                    numberOfInputs = totalTrainingPoints;
                }
                int vectorMax = 0;
                int zero = 0, one = 0, two = 0, three = 0, four = 0, five = 0, six = 0, seven = 0, eight = 0, nine = 0;
                int zeroR = 0, oneR = 0, twoR = 0, threeR = 0, fourR = 0, fiveR = 0, sixR = 0, sevenR = 0, eightR = 0, nineR = 0;
                int numPoints = 0;
                for (int i = 0; i < numberOfInputs; i++) {
                    for (int j = 0; j < numInputs; j++) {
                        if(choice == 3){
                            network[0].vector.setMatData(j, 0, vScanVals[i][j + 1]);

                        } else {
                            network[0].vector.setMatData(j, 0, testingSet[i][j + 1]);
                        }
                    }
                    for (int j = 0; j < numLayers - 1; j++) {
                        network[j + 1].vector = network[j].calculateNext();
                    }
                    for (int j = 0; j < network[network.length - 1].vector.numColumn; j++) {
                        if (network[network.length - 1].vector.getMatData(j, 0) > network[network.length - 1].vector.getMatData(vectorMax, 0)) {
                            vectorMax = j;
                        }
                    }

                    if (choice == 5) {
                        System.out.println("Number seen: " + vectorMax + "\tCorrect Identification: " + testingSet[i][0]);
                        String s = printNumber(testingSet[i]);
                        if(s.equals("S")){
                            break;
                        }
                    }

                    if (choice == 6) {
                        if ((int) testingSet[i][0] != vectorMax) {
                            System.out.println("Number seen: " + vectorMax + "\tCorrect Identification: " + testingSet[i][0]);
                            String s = printNumber(testingSet[i]);
                            if(s.equals("S")){
                                break;
                            }
                        }
                    }
                    if(choice == 3){
                        switch ((int) vScanVals[i][0]) {
                            case 0:
                                zeroR++;
                                break;
                            case 1:
                                oneR++;
                                break;
                            case 2:
                                twoR++;
                                break;
                            case 3:
                                threeR++;
                                break;
                            case 4:
                                fourR++;
                                break;
                            case 5:
                                fiveR++;
                                break;
                            case 6:
                                sixR++;
                                break;
                            case 7:
                                sevenR++;
                                break;
                            case 8:
                                eightR++;
                                break;
                            case 9:
                                nineR++;
                                break;
                        }
                        if(vScanVals[i][0] == vectorMax){
                            error++;
                            numPoints = vScanVals.length;
                        }
                    } else {
                        switch ((int) testingSet[i][0]) {
                            case 0:
                                zeroR++;
                                break;
                            case 1:
                                oneR++;
                                break;
                            case 2:
                                twoR++;
                                break;
                            case 3:
                                threeR++;
                                break;
                            case 4:
                                fourR++;
                                break;
                            case 5:
                                fiveR++;
                                break;
                            case 6:
                                sixR++;
                                break;
                            case 7:
                                sevenR++;
                                break;
                            case 8:
                                eightR++;
                                break;
                            case 9:
                                nineR++;
                                break;
                        }
                        if(testingSet[i][0] == vectorMax){
                            error++;
                            numPoints = testingSet.length;
                        }
                    }

                    switch (vectorMax) {
                        case 0:
                            zero++;
                            break;
                        case 1:
                            one++;
                            break;
                        case 2:
                            two++;
                            break;
                        case 3:
                            three++;
                            break;
                        case 4:
                            four++;
                            break;
                        case 5:
                            five++;
                            break;
                        case 6:
                            six++;
                            break;
                        case 7:
                            seven++;
                            break;
                        case 8:
                            eight++;
                            break;
                        case 9:
                            nine++;
                            break;
                    }
                }
                System.out.println("Accuracy = " + error + "/" + numPoints + " = " + ((double) error / numPoints));
                error = 0;
                System.out.println("1 = " + one + "/" + oneR + "\t2 = " + two + "/" + twoR + "\t3 = " + three + "/" + threeR + "\t4 = " + four + "/" + fourR + "\t5 = " + five + "/" + fiveR);
                System.out.println("6 = " + six + "/" + sixR + "\t7 = " + seven + "/" + sevenR + "\t8 = " + eight + "/" + eightR + "\t9 = " + nine + "/" + nineR + "\t0 = " + zero + "/" + zeroR);
            }

            if (choice == 7) {
                writeToCsv(network, "w", System.getProperty("user.dir") + "/weights.csv");
                writeToCsv(network, "b", System.getProperty("user.dir") + "/biases.csv");
            }
        }
    }

    public static int initProgram() {
        System.out.print("Welcome to Christian Halls 475 neural network program, The main function of this network ");
        System.out.println("is to take the data from the MNIST data set and learn to recognize digits 0-9 with it.\n");

        System.out.println("Please select what you would like this program to do\n\n");

        System.out.println("[0] : Exit the program");
        System.out.println("[1] : Train a new network");
        System.out.println("[2] : Load a pre-trained network\n");

        Scanner scanner = new Scanner(System.in);
        return scanner.nextInt();
    }

    public static int contProgram(){
        System.out.println("[0] : Exit the program");
        System.out.println("[1] : Train a new network");
        System.out.println("[2] : Load a pre-trained network");
        System.out.println("[3] : Display network accuracy on TRAINING data");
        System.out.println("[4] : Run network on TESTING data");
        System.out.println("[5] : Run network on TESTING data showing images and lables");
        System.out.println("[6] : Display the misclassified TESTING images");
        System.out.println("[7] : Save the network state to file");

        Scanner scanner = new Scanner(System.in);
        return scanner.nextInt();
    }

    public static String printNumber(double[] vector){
        for(int i = 0; i < 28; i++){
            for(int j = 0; j < 28; j++){
                if(vector[(i*28)+j + 1] > 0){
                    System.out.print("&");
                } else {
                    System.out.print(" ");
                }
            }
            System.out.println("");
        }
        System.out.println("\nPress enter to view next image\t Enter S to stop");
        Scanner scanner = new Scanner(System.in);
        return scanner.nextLine();
    }

    public static void writeToCsv(Layer[] inputLayer, String type, String fileName) {
        try (FileWriter writer = new FileWriter(fileName)) {
            for(int i = 0; i < inputLayer.length - 1; i++) {
                if(type.equals("w")) {
                    for (int j = 0; j < inputLayer[i].weights.numColumn * inputLayer[i].weights.numRow; j++) {
                        writer.append(inputLayer[i].weights.getMatData((int) j / (inputLayer[i].weights.numRow), j % inputLayer[i].weights.numRow) + "");
                        if (j + 1 < inputLayer[i].weights.numColumn * inputLayer[i].weights.numRow) {
                            writer.append(",");
                        }
                    }
                }
                if(type.equals("b")){
                    for(int j = 0; j < inputLayer[i].bias.numColumn; j++){
                        writer.append(inputLayer[i].bias.getMatData(j,0) + "");
                        if(j+1 < inputLayer[i].bias.numColumn){
                            writer.append(",");
                        }
                    }
                }
                writer.append("\n");
            }

        } catch (IOException e){
            System.out.println("Please close the file: " + fileName);
            System.exit(0);
        }
    }
}

class Layer{
    public Matrix weights;
    public Matrix vector;
    public Matrix bias;
    public Matrix biasGradient;
    public Matrix weightGradient;

    // Init function for layer class
    public Layer(Matrix weights, Matrix vector, Matrix bias, Matrix biasGradient, Matrix weightGradient){
        // if the layer is the last layer, we only need the activation layer from it. everything else can be null
        if(weights == null && bias == null){
            this.weights = null;
            this.vector = vector;
            this.bias = null;
            this.biasGradient = null;
            this.weightGradient = null;
        }
        // initialize all the data for the layers!
        else if(weights.numRow == vector.numColumn){
            this.weights = weights;
            this.vector = vector;
            this.bias = bias;
            this.biasGradient = biasGradient;
            this.weightGradient = weightGradient;

        }
        else {
            System.out.println("To make a proper neural network Layer the number of rows in weights must be the same as the number of columns in vector");
        }
    }

    // take the weights and multiply them by the vector, return the resulting vector
    public Matrix calculateNext(){
        Matrix output = weights.multiply(vector);
        output = output.add(bias);
        output.sigmoid();
        return output;
    }

    // take the weight gradient and add it to the weights, set these to the new weights
    public void calculateNewWeights(double learningRate, int sizeOfData){
        Matrix output = new Matrix(weights.numColumn, weights.numRow);
        for(int i = 0; i < output.numColumn; i++){
            for(int j = 0; j < output.numRow; j++){
                double val = weights.getMatData()[i][j] - (learningRate/sizeOfData) * weightGradient.getMatData()[i][j];
                output.setMatData(i,j, val);
            }
        }
        weights = output;
    }

    // take the bias gradient and add it to the old biases, set these equal to the new biases
    public void calculateNewBiases(double learningRate, int sizeOfData){
        Matrix output = new Matrix(bias.numColumn, bias.numRow);
        for(int i = 0; i < output.numColumn; i++){
            double val = bias.getMatData()[i][0] - (learningRate/sizeOfData) * biasGradient.getMatData()[i][0];
            output.setMatData(i,0, val);
        }
        bias = output;
    }

    // toString that returns a layer in the format
    // Vector:
    // [all values seperated by a line break as seen in matrix]
    // Weights:
    // [all values seperated by a line break as seen in matrix]
    // Biases:
    // [all values seperated by a line break as seen in matrix]
    // BiasGradient:
    // [all values seperated by a line break as seen in matrix]
    // WeightGradient:
    // [all values seperated by a line break as seen in matrix]
    public String toString(){
        return "Vector:\n" + vector + "\n\n Weights:\n" + weights + "\n\n Biases:\n" + bias + "\n\n BiasGradient:\n" + biasGradient + "\n\n WeightGradient:\n" + weightGradient;
    }

}

class Matrix{
    private double[][] matData; // all matData needs to be changed to float
    public int numColumn;
    public int numRow;

    // INIT function for the matrix class. creates a Double array and also saves the number of row and collumns
    public Matrix(int numColumn, int numRow){
        double[][] matData = new double[numColumn][numRow]; // all matData needs to be changed to float
        this.matData = matData;
        this.numColumn = numColumn;
        this.numRow = numRow;
    }

    // Format: <Matrix>.getMatData(column, row)
    // Purpose: return a single index from the Matrix at index Matrix[column][row]
    public double getMatData(int column, int row){
        return matData[column][row];
    }

    // Format: <Matrix>.getMatData()
    // Purpose: returns the entire matrix as a 2d Double array
    public double[][] getMatData(){
        return matData;
    }

    // Format: <Matrix>.setMatData(<2DDoubleArray>)
    // Purpose: Sets the Matrix equal to the 2D arrays
    public void setMatData(double[][] newData){
        if (matData.length == newData.length && matData[0].length == newData[0].length){
            for(int i = 0; i < newData.length; i++){
                for(int j = 0; j < newData[i].length; j++){
                    matData[i][j] = newData[i][j];
                }
            }
        }
        else{
            System.out.println("Please enter a Matrix that will fit in the the bounds of a " + matData.length + "x" + matData[0].length + " Matrix");
        }
    }

    // Format: <Matrix>.setMatData()
    // Purpose: place 1 double at one specific point in a matrix
    public void setMatData(int row, int column, double number){
        matData[row][column] = number;
    }


    // Format: <Matrix1>.multiply(<Matrix2>)
    // Purpose: Multiply an NxM and an MxO matrix to make a NxO matrix
    public Matrix multiply(Matrix m2){
        Matrix output = new Matrix(matData.length, m2.getMatData()[0].length);
        // conditions: the OG Matrix must have the same number of rows as the input Matrix does columns
        if(matData[0].length == m2.getMatData().length){
            double matNumber = 0; // needs to be changed to float
            for(int i = 0; i < matData.length; i++){
                for(int j = 0; j < m2.getMatData()[0].length; j++){
                    for(int k = 0; k < m2.getMatData().length; k++){
                        matNumber += matData[i][k] * m2.getMatData()[k][j];
                    }
                    output.setMatData(i,j,matNumber);
                    matNumber = 0;
                }
            }
        }
        else if (matData[0].length != m2.getMatData().length){
            System.out.println("number of columns in Matrix 1 doesn't match number of rows in Matrix 2");
            return null;
        }
        else{
            System.out.println("error in multiply function Matrix class");
        }
        return output;
    }

    // Format: <Matrix1>.add(<Matrix2>);
    // Purpose: takes two Matrixes and adds them together, the return value is the sum of the matrices
    public Matrix add(Matrix m2){
        // conditions: this.Matrix must be the same size as m2 otherwise throw an error
        Matrix output = new Matrix(matData.length, matData[0].length);
        if (m2.matData.length == matData.length && m2.matData[0].length == matData[0].length){
            for(int i = 0; i < matData.length; i++){
                for(int j = 0; j < matData[i].length; j++){
                    output.setMatData(i,j,matData[i][j] + m2.matData[i][j]);
                }
            }
        }
        return output;
    }

    // format: <Matrix>.transpose()
    // Purpose: returns the transpostions of the inputed Matrix
    public Matrix transpose(){
        Matrix output = new Matrix(numRow, numColumn);
            for(int i = 0; i < numColumn; i++){
                for (int j = 0; j < numRow; j++){
                    output.matData[i][j] = matData[j][i];
                }
            }
            return output;
    }

    // Format: <Matrix>.sigmoid
    // Purpose: Change any values in given Matrix into a value from 0-1 based on the sigmoid function
    public void sigmoid(){
        for(int i = 0; i < numColumn; i++) {
            for (int j = 0; j < numRow; j++) {
                matData[i][j] = 1 / (1 + Math.exp(-1 * matData[i][j]));
            }
        }
    }

    // toString returns the data in a matrix in the format...
    //  1   2   3
    //  4   5   6
    //  7   8   9
    public String toString(){
        String output = "";
        for(int i = 0; i < matData.length; i++){
            for(int j = 0; j < matData[i].length; j++){
                output += matData[i][j] + "\t";
            }
            output += "\n";
        }
        return output;
    }
}