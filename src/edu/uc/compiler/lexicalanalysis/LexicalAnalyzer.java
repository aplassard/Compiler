package edu.uc.compiler.lexicalanalysis;

import edu.uc.compiler.utils.ParseArgs;

public class LexicalAnalyzer {
	private Scanner scanner;
	private boolean initialized;
	private boolean verbose=false;
	
	public LexicalAnalyzer(ParseArgs args){
		initialize(args.fileName,args.verboseLexicalAnalysis);
	}

	/**
	 * @return the scanner
	 */
	public Scanner getScanner() {
		return scanner;
	}
	
	public void initialize(String filename, boolean verbose){
		this.scanner = new Scanner(filename);
		this.verbose = verbose;
		if(this.scanner.isInitialized()) initialized = true;
		else initialized = false;
	}
	
	public boolean isInitialized(){
		return initialized;
	}

}
