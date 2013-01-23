package edu.uc.compiler.exception;

abstract class BadToken extends Exception {

	/**
	 * 
	 */
	private static final long serialVersionUID = 1L;
	
	public BadToken(String message){
		super(message);
	}

}
