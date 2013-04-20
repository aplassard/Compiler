package edu.uc.compiler.lexicalanalysis;

import edu.uc.compiler.exception.BadToken;
import edu.uc.compiler.exception.InvalidString;

public abstract class TokenGenerator {
	public Scanner scanner;
	public String word;
	public Token T;
	public abstract Token getToken() throws BadToken;
	public void makeToken(Tag t){
		T.setTagType(t);
		T.setText(word);
	}
	TokenGenerator(Scanner s, char r) {
		this.scanner = s;
		this.word = String.valueOf(r);
		this.T = new Token();
	}
	
	public boolean isSomething(char c){
		return (c==')'||c=='{'||c=='('||c=='='||c=='}'||c==';'||c=='+'||c=='-'||c=='/'||c=='*'||c=='>'||c=='<'||c==':'||c=='"');
	}
}
