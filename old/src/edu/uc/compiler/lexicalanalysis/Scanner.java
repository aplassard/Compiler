package edu.uc.compiler.lexicalanalysis;

import java.io.*;

public class Scanner {
	private PushbackReader sourceFile;
	private String fileName;
	private boolean initialized;
	private int lineNumber;
	
	/**
	 * Default constructor for Scanner
	 */
	public Scanner(String filename){
		initialize(filename);
	}
	
	/**
	 * @return the sourceFile
	 */
	public PushbackReader getSourceFile() {
		return sourceFile;
	}
	
	public void initialize(String filename){
		this.fileName = filename;
		try {
			this.sourceFile = new PushbackReader(new FileReader(filename));
		} catch (FileNotFoundException e) {
			e.printStackTrace();
			this.initialized = false;
			return;
		}
		this.lineNumber = 1;
		this.initialized = true;
	}

	/**
	 * @return the initialized
	 */
	public boolean isInitialized() {
		return initialized;
	}

	/**
	 * @return the fileName
	 */
	public String getFileName() {
		return fileName;
	}

	public int getLineNumber(){
		return lineNumber;
	}
	
	public void iterateLineNumber(){
		lineNumber++;
	}
	
	public int getNextChar() throws IOException{
		return this.sourceFile.read();
	}
	
	public void readUntilNewLine() throws IOException{
		char c = (char) getNextChar();
		while(c!='\n'&&c!='\r'){
			c = (char) getNextChar();
		}
		iterateLineNumber();
		return;
	}
	
	public void pushBack(char c){
		try {
			this.sourceFile.unread((int) c);
		} catch (IOException e) {
			// TODO Auto-generated catch block
			e.printStackTrace();
		}
	}
}
