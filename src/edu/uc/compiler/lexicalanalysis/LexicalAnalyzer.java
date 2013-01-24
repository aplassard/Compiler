package edu.uc.compiler.lexicalanalysis;

import java.io.IOException;
import java.util.ArrayList;
import java.util.List;
import edu.uc.compiler.CompilerMain;

import edu.uc.compiler.utils.ParseArgs;
import edu.uc.compiler.exception.BadToken;
import edu.uc.compiler.exception.InvalidString;
import edu.uc.compiler.exception.UnexpectedFileEnd;
import edu.uc.compiler.exception.InvalidNumber;

import edu.uc.compiler.CompilerMain;

public class LexicalAnalyzer {
	private Scanner scanner;
	private boolean initialized;
	private boolean verbose=false;
	private boolean EOF=true;
	private List<Token> tokens;
	public char c;
	private String word;
	
	public LexicalAnalyzer(ParseArgs args){
		initialize(args.fileName,args.verboseLexicalAnalysis);
	}

	public Scanner getScanner() {
		return scanner;
	}
	
	public void initialize(String filename, boolean verbose){
		this.scanner = new Scanner(filename);
		this.verbose = verbose;
		this.tokens = new ArrayList<Token>();
		if(this.scanner.isInitialized()) initialized = true;
		else initialized = false;
	}
	
	public boolean isInitialized(){
		return initialized;
	}
	
	public boolean hasNext(){
		return EOF;
	}
	
	public Token getNextToken() throws UnexpectedFileEnd, BadToken{
		Token T=null;
		try {
			int n = this.scanner.getNextChar();
			this.c = (char) n;
			while(Character.isWhitespace(c)){
				n = this.scanner.getNextChar();
				if(n==65535) throw new UnexpectedFileEnd("File end found at line " + scanner.getLineNumber()+".  \"EOF\" not found.");
				else if(c=='\n'){
					System.out.println("Called iterate from getNextToken()");
					this.scanner.iterateLineNumber();
				}
				c = (char) n;
			}
		} catch (IOException e) {
			e.printStackTrace();
			this.EOF=true;
		}
		if(Character.isDigit(c)) T = parseNum();
		else if(Character.isLetter(c)) T = parseLetter();
		else if((int)c==65535) throw new UnexpectedFileEnd("File end found at line " + scanner.getLineNumber()+".  \"EOF\" not found.");
		else{
			T=new Token();
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
					T.setTagType(Tag.DIVIDE);
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
		}
		if(T!=null){
			tokens.add(T);
			if(verbose) printToken(T);
		}
		return T;
	}

	private Token parseColon() {
		this.word = String.valueOf(c);
		try {
			c = (char) this.scanner.getNextChar();
		} catch (IOException e) {
			e.printStackTrace();
		}
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
	}

	private Token parseNum() throws InvalidNumber {
		Token T = new Token();
		try {
			int n = this.scanner.getNextChar();
			this.word = String.valueOf(c);
			while(n!=-1){
				c = (char) n;
				if(Character.isDigit(c)) word.concat(String.valueOf(c));
				else if(c=='.'&& !word.contains("."))this.word= this.word.concat(String.valueOf(c));
				else if(c==')'||c==';'){
					this.scanner.pushBack(c);
					break;
				}
				else{
					scanner.readUntilNewLine();
					BadToken E =  new InvalidNumber("Invalid number token found at line: "+this.scanner.getLineNumber());
					E.s=word;
					throw (InvalidNumber) E;
				}
			}
		} catch (IOException e) {
			e.printStackTrace();
		}
		T.setText(word);
		T.setTagType(Tag.NUMBER);
		this.word="";
		return T;
	}
	
	private Token parseLetter() throws InvalidString{
		Token T = new Token();
		T.setTagType(Tag.IDENTIFIER);
		try {
			this.word = "";
			while(!Character.isWhitespace(c)){
				this.word=this.word.concat(String.valueOf(c));
				c = (char) this.scanner.getNextChar();
				if(!Character.isLetterOrDigit(c)&&c!='_'&&!Character.isWhitespace(c)&&c!='('){
					BadToken E =  new InvalidString("Invalid string token found at line: "+this.scanner.getLineNumber());
					E.s=word;
					throw (InvalidString) E;
				}
				else if(c=='('){
					this.scanner.pushBack(c);
					break;
				}
				
				
			}
		} catch (IOException e) {
			e.printStackTrace();
		}
		T.setText(word);
		this.tokens.add(T);
		this.word="";
		if(c=='\n'){
			this.scanner.iterateLineNumber();
		}
		return T;
	}
	
	public void printToken(Token T){
		CompilerMain.printOutput("Token "+T.toString()+" at line "+this.scanner.getLineNumber());
	}
}
