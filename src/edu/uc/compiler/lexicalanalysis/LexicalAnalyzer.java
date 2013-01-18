package edu.uc.compiler.lexicalanalysis;

import java.io.IOException;

import edu.uc.compiler.utils.ParseArgs;
import edu.uc.compiler.exception.UnexpectedFileEnd;

public class LexicalAnalyzer {
	private Scanner scanner;
	private boolean initialized;
	private boolean verbose=false;
	private boolean EOF=false;
	
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
	public boolean hasNext(){
		return EOF;
	}
	public Token getNextToken() throws UnexpectedFileEnd{
		Token T = new Token();
		try {
			int n = this.scanner.getNextChar();
			char c = (char) n;
			while(Character.isWhitespace(c)){
				n = this.scanner.getNextChar();
				if(n==-1) throw new UnexpectedFileEnd("File end found at line " + scanner.getLineNumber()+".  \"EOF\" not found.");
				c = (char) n;
			}
		} catch (IOException e) {
			e.printStackTrace();
			this.EOF=true;
		}
		return T;
	}

}
