package edu.uc.compiler.exception;

public abstract class BadToken extends Exception {

	/**
	 * 
	 */
	public String s;
	public String b;
	private static final long serialVersionUID = 1L;
	
	public BadToken(String message){
		super(message);
	}

}
