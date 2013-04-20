package edu.uc.compiler.parser.ast.expression;

import java.util.ArrayList;

public class NonTerminalExpression extends Expr {

	private ArrayList<CompoundExpression> Accepts;
	
	public NonTerminalExpression(ArrayList<CompoundExpression> Accepts) {
		this.Accepts = Accepts;
	}

}
