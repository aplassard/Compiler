package edu.uc.compiler.lexicalanalysis;


public class Token {

	private String text="";
	private Tag tagType;
	
	public void setText(String text){
		this.text = text;
	}
	
	public void setTagType(Tag tagType){
		this.tagType = tagType;
	}
	
	public String toString(){
		return "<" + this.text + "," + this.tagType + ">";
	}
	
}
