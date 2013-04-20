package edu.uc.compiler.utils;

public class ParseArgs {
	
	public boolean verboseLexicalAnalysis = false;
	public String fileName;
	public String[] inputArgs;
	
	public ParseArgs(String[] input){
		inputArgs = input;
		if(inputArgs.length < 2){ 
			printUsage();
		}
		else{
			for(int i =0; i < inputArgs.length; i++){
				if(inputArgs[i].equals("-f")||inputArgs[i].equals("--file-name")){
					i++;
					this.fileName = inputArgs[i];
				}
				else if(inputArgs[i].equals("-l")||inputArgs[i].equals("--verbose-lexical-analysis")) this.verboseLexicalAnalysis = true;
				else printError(inputArgs[i]);
			}
			if(fileName == null) printNoFile();
		}
	}
	
	public void printUsage(){
		System.out.println("Command Line Arguments:");
		System.out.println("\t-f/--file-name <source file> (required)");
		System.out.println("\t-l/--verbose-lexical-analysis");
		System.exit(1);
	}
	
	public void printError(String badArg){
		System.out.println("Error!  Cannot find arguement: "+badArg);
		printUsage();
	}
	
	public void printNoFile(){
		System.out.println("Error!  File not defined!");
		printUsage();
	}
}
