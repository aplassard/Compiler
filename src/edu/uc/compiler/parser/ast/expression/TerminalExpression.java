package edu.uc.compiler.parser.ast.expression;

import edu.uc.compiler.lexicalanalysis.Tag;

public class TerminalExpression extends Expr {

	private Tag Accepts;
	
	public TerminalExpression(Tag A) {
		this.Accepts = A;
	}

	public boolean equals(Tag T){
		return T.equals(Accepts);
	}
}
