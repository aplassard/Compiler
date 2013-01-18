package edu.uc.compiler.lexicalanalysis;

import java.io.*;

public class Scanner {
	private BufferedReader sourceFile;
	private String fileName;
	private boolean initialized;
	
	/**
	 * Default constructor for Scanner
	 */
	public Scanner(String filename){
		initialize(filename);
	}
	
	/**
	 * @return the sourceFile
	 */
	public BufferedReader getSourceFile() {
		return sourceFile;
	}
	
	public void initialize(String filename){
		this.fileName = filename;
		try {
			this.sourceFile = new BufferedReader(new FileReader(filename));
		} catch (FileNotFoundException e) {
			e.printStackTrace();
			this.initialized = false;
			return;
		}
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


}
