Compiler Description
Andrew Plassard

	to build:
		./build.sh
			or
		jar cfm compiler.jar META_INF/MANIFEST.MF *

	usage:
		java -jar compiler.jar -j <input_file>

	options:
		-l / --verbose-lexical-analysis (output verbose lexical analysis)

	Lexical Analyzer:
		Lexical Analyzer is generated in edu.uc.compiler.CompilerMain.  Lexical Analysis occurs through a scanner reading the file character by character.  The lexical analyzer decides what class of token an incoming token is based on the first element (number, string, keyword, symbol).  The lexical analyzer then creates a new class that has extended the tokengetter interface.  This then works with the scanner to pull as much from the file as necessary.  If excess information is pulled, the scanner allows for pushback as well.  The scanner maintains the current line number and as a Token is created, it also keeps the time number.
