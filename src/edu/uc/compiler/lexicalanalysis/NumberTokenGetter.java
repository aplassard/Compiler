package edu.uc.compiler.lexicalanalysis;

import edu.uc.compiler.exception.BadToken;

public class NumberTokenGetter extends TokenGenerator {

	public NumberTokenGetter(Scanner s, char r) {
		super(s, r);
	}

	@Override
	public Token getToken() throws BadToken {
		return null;
	}

}
