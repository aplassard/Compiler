package edu.uc.compiler.lexicalanalysis;

public enum Tag {
	
	STRING("string","word"),
	CASE("case","word"),
	INT("int","word"),
	FOR("for","word"),
	BOOL("bool","word"),
	AND("and","word"),
	FLOAT("float","word"),
	OR("or","word"),
	GLOBAL("global","word"),
	NOT("not","word"),
	IN("in","word"),
	PROGRAM("program","word"),
	OUT("out","word"),
	PROCEDURE("procedure","word"),
	IF("if","word"),
	BEGIN("begin","word"),
	THEN("then","word"),
	RETURN("return","word"),
	ELSE("else","word"),
	END("end","word"),
	COLON(":","colon"),
	SEMICOLON(";","semicolon"),
	COMMA(",","comma"),
	PLUS("+","plus"),
	MINUS("-","minus"),
	MULTIPLY("*","mulitplication"),
	DIVIDE("/","division"),
	L_PAREN("(","L_paren"),
	R_PAREN(")","R_paren"),
	LT("<","Less_Than"),
	GT(">","Greater_Than"),
	LTE("<=","Less_Than_or_Equal_to"),
	GTE(">=","Greater_Than_or_Equal_to"),
	N_EQUAL("!=","Not_Equal"),
	EQUAL("=","Equal"),
	SET_VAL(":=","Set_Value"),
	L_BRACE("{","L_Brace"),
	R_BRACE("}","R_Brace"),
	IDENTIFIER("[a-zA-Z][a-zA-Z0-9_]*","identifier"),
	QSTRING("\"[a-zA-Z0-9 _,;:.']*\"","Quoted_String"),
	EOF("EOF","End_of_File"),
	NUMBER("[0-9][0-9]*[.[0-9]*]?","Number");
	
	
	private final String accepts;
	private final String text;
	
	Tag(String accepts, String text){
		this.accepts = accepts;
		this.text = text;
	}
	
	public String toString(){
		return this.text;
	}
	
}
