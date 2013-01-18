package edu.uc.compiler.lexicalanalysis;


public class LexicalAnalysis {
	private Scanner scanner;
	private boolean initialized;

	/**
	 * @return the scanner
	 */
	public Scanner getScanner() {
		return scanner;
	}
	
	public void initialize(String filename){
		this.scanner = new Scanner(filename);
		if(this.scanner.isInitialized()) initialized = true;
		else initialized = false;
	}
	
	public boolean isInitialized(){
		return initialized;
	}

}