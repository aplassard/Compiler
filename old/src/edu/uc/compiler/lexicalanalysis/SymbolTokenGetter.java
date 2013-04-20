package edu.uc.compiler.lexicalanalysis;

import java.io.IOException;

import edu.uc.compiler.CompilerMain;
import edu.uc.compiler.exception.BadToken;

public class SymbolTokenGetter extends TokenGenerator {

	public SymbolTokenGetter(Scanner s, char r) {
		super(s, r);
	}

	@Override
	public Token getToken() throws BadToken {
		char c = word.charAt(0);
		switch(c){
			case ':':
				T=parseColon();
				break;
			case ';':
				T.setText(";");
				T.setTagType(Tag.SEMICOLON);
				break;
			case ',':
				T.setText(",");
				T.setTagType(Tag.COMMA);
				break;
			case '+':
				T.setText("+");
				T.setTagType(Tag.PLUS);
				break;
			case '-':
				T.setText("-");
				T.setTagType(Tag.MINUS);
				break;
			case '*':
				T.setText("*");
				T.setTagType(Tag.MULTIPLY);
				break;
			case '/':
				T.setText("/");
				T=parseDivide();
				break;
			case '(':
				T.setText("(");
				T.setTagType(Tag.L_PAREN);
				break;
			case ')':
				T.setText(")");
				T.setTagType(Tag.R_PAREN);
				break;
			case '{':
				T.setText("{");
				T.setTagType(Tag.L_BRACE);
				break;
			case '}':
				T.setText("}");
				T.setTagType(Tag.R_BRACE);
				break;
			case '=':
				T.setText("=");
				T.setTagType(Tag.EQUAL);
				break;
			default:
				CompilerMain.printWarning("Unidentified object in file: "+String.valueOf(c)+" at line "+this.scanner.getLineNumber());
				return null;	
		}
		return T;
	}

	private Token parseColon() {
		char c;
		try {
			c = (char) this.scanner.getNextChar();
			Token T = new Token();
			T.setTagType(Tag.COLON);
			if(c=='='){
				this.word = this.word.concat(String.valueOf(c));
				T.setTagType(Tag.SET_VAL);
				
			}
			else{
				this.scanner.pushBack(c);
			}
			return T;
		} catch (IOException e) {
			e.printStackTrace();
			return null;
		}
	}

	private Token parseDivide() {
		char c;
		try {
			c = (char) this.scanner.getNextChar();
			Token T = new Token();
			T.setTagType(Tag.DIVIDE);
			if(c=='/'){
				this.word = this.word.concat(String.valueOf(c));
				T.setTagType(Tag.COMMENT);
				while(c!='\n'){
					this.word.concat(String.valueOf(c));
					c = (char) this.scanner.getNextChar();
				}
			}
			else{
				this.scanner.pushBack(c);
			}
			return T;
		} catch (IOException e) {
			e.printStackTrace();
			return null;
		}
	}
}
