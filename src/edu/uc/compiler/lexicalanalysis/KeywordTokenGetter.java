package edu.uc.compiler.lexicalanalysis;

import java.io.IOException;

import edu.uc.compiler.exception.BadToken;
import edu.uc.compiler.exception.InvalidKeyword;

public class KeywordTokenGetter extends TokenGenerator {

	KeywordTokenGetter(Scanner s, char r) {
		super(s, r);
	}

	@Override
	public Token getToken() throws InvalidKeyword {
		parseKeyword();
		return T;
	}
	
	private Token parseKeyword() throws InvalidKeyword{
		try {
			char c = (char) this.scanner.getNextChar();
			while(true){
				if(Character.isWhitespace(c)){
					determineTag();
					return this.T;
				}
				else if(isSomething(c)){
					this.scanner.pushBack(c);
					determineTag();
					return this.T;
				}
				else if(!Character.isLetterOrDigit(c)&&c!='_'){
					BadToken E = new InvalidKeyword("Invalid keyword token found at line: "+this.scanner.getLineNumber());
					E.s=word;
					E.b = String.valueOf(c);
					throw (InvalidKeyword) E;
				}
				else{
					this.word = this.word.concat(String.valueOf(c));
					c = (char) this.scanner.getNextChar();
				}
				
			}
		} catch (IOException e) {
			e.printStackTrace();
		}
		return this.T;
	}
	
	private void determineTag(){
		for(Tag t: Tag.values()){
			if(equals(t.accepts(word))){
				makeToken(t);
				return;
			}
			else{
				makeToken(Tag.IDENTIFIER);
				return;
			}
		}
	}

}
