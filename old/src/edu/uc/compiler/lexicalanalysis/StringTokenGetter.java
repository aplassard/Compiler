package edu.uc.compiler.lexicalanalysis;

import edu.uc.compiler.exception.BadToken;
import edu.uc.compiler.exception.InvalidString;

public class StringTokenGetter extends TokenGenerator {

	public StringTokenGetter(Scanner s, char r) {
		super(s, r);
	}

	@Override
	public Token getToken() throws BadToken {
		try{
			char c = (char) this.scanner.getNextChar();
			while(true){
				if(c=='\n'){
					BadToken E = new InvalidString("Invalid string token found a line: "+this.scanner.getLineNumber());
					E.s=word;
					E.b="\\n";
					this.scanner.pushBack(c);
					throw (InvalidString) E;
				}
				else if(c=='"'){
					this.word = this.word.concat(String.valueOf(c));
					this.T.setText(word);
					this.T.setTagType(Tag.QSTRING);
					return this.T;
				}
				else{
					this.word = this.word.concat(String.valueOf(c));
					c = (char) this.scanner.getNextChar();
				}
			}
		}
		catch(Exception e){
			e.printStackTrace();
		}
		return null;
	}

}
