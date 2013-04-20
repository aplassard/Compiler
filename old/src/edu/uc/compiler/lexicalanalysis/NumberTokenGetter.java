package edu.uc.compiler.lexicalanalysis;

import edu.uc.compiler.exception.BadToken;
import edu.uc.compiler.exception.InvalidNumber;

public class NumberTokenGetter extends TokenGenerator {

	public NumberTokenGetter(Scanner s, char r) {
		super(s, r);
	}

	@Override
	public Token getToken() throws InvalidNumber {
		try{
			char c = (char) this.scanner.getNextChar();
			while(true){
				if(Character.isWhitespace(c)){
					this.T.setText(word);
					this.T.setTagType(Tag.NUMBER);
					this.scanner.pushBack(c);
					return this.T;
				}
				else if(isSomething(c)){
					this.scanner.pushBack(c);
					this.T.setText(word);
					this.T.setTagType(Tag.NUMBER);
					return this.T;
				}
				else if(Character.isDigit(c)){
					c=(char)this.scanner.getNextChar();
				}
				else{
					BadToken E = new InvalidNumber("Invalid number token found at line: "+this.scanner.getLineNumber());
					E.s=word;
					E.b = String.valueOf(c);
					throw (InvalidNumber) E;
				}
			}
		}
		catch(Exception e){
			e.printStackTrace();
		}
		return null;
	}

}
