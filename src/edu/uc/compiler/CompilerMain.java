package edu.uc.compiler;

import edu.uc.compiler.exception.BadToken;
import edu.uc.compiler.exception.UnexpectedFileEnd;
import edu.uc.compiler.lexicalanalysis.LexicalAnalyzer;
import edu.uc.compiler.lexicalanalysis.Token;
import edu.uc.compiler.utils.ParseArgs;

public class CompilerMain {

	/**
	 * @param args
	 */
	public static void main(String[] args) {
		ParseArgs arguements = new ParseArgs(args);
		LexicalAnalyzer LA = new LexicalAnalyzer(arguements);
		if(!LA.isInitialized()){
			System.out.println("There is an error and the system is not initialized");
			System.out.println("Exitting now");
			System.exit(1);
		}
		Token T;
		while(LA.hasNext()){
			try {
				try {
					T = LA.getNextToken();
				} catch (BadToken e) {
					printWarning("Couldn't figure this one out.  This is what I had so far: "+e.s+".  This is what I couldn't figure out: "+e.b+".");
				}
			} catch (UnexpectedFileEnd e) {
				e.printStackTrace();
				break;
			}
		}
	}
	
	public static void printError(String error){
		System.out.println("Error: " + error);
	}
	public static void printOutput(String output){
		System.out.println("Output: " + output);
	}
	public static void printWarning(String warning){
		System.out.println("Warning: "+warning);
	}

}
