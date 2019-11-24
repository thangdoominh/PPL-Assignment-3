// Name: Ho Minh Hoang
// Student's ID: 1710094
grammar MC;

@lexer::header {
from lexererr import *
}

@lexer::member {
def emit(self):
    tk = self.type
    if tk == UNCLOSE_STRING:
        result = super.emit();
        raise UncloseString(result.text);
    elif tk == ILLEGAL_ESCAPE:
        result = super.emit();
        raise IllegalEscape(result.text);
    elif tk == ERROR_CHAR:
        result = super.emit();
        raise ErrorToken(result.text);
    else:
        return super.emit();
}

options{
	language=Python3;
}

program  : manydeclares EOF ;
manydeclares: declare+ ;
declare: vardec | funcdec ;

//variable declarations
vardec: primetype manyvar SEMI ;
manyvar: var (COMMA var)* ;
var: ID | array ;
array: ID LSB INTLIT RSB;
//function declarations
funcdec: mctype ID LB paralist? RB stmtblock;
mctype: primetype | arraypointer | VOIDTYPE;
//array
arraypointer: ( BOOLTYPE | INTTYPE | FLOATTYPE | STRTYPE ) LSB RSB ;
//parameter
paralist: para (COMMA para)* ;
para: primetype (ID | ID LSB RSB) ;
//block stament
memblock: stmts | vardec ;
stmtblock: LP memblock* RP ;
stmts: do_whilestmt | ifstmt | forstmt | retstmt | (exp SEMI) | stmtblock | breakstmt | continuestmt  ;

//if stament
ifstmt: IF LB exp RB stmts (ELSE stmts)? ;
//do while stament
do_whilestmt: DO stmts+ WHILE exp SEMI ;
// for stament
forstmt: FOR LB exp SEMI exp SEMI exp RB stmts;
//break stament
breakstmt: BREAK SEMI ;
//continue stament
continuestmt: CONTINUE SEMI ;
//return stament
retstmt: RETURN exp? SEMI ;

//main function
//mainfunc: VOIDTYPE 'main' LB RB stmtblock ;

//expression
exp: exp1 ASSOP exp | exp1 ;
exp1: exp1 OROP exp2 | exp2 ;
exp2: exp2 ANDOP exp3 | exp3 ;
exp3: exp4 EQOP exp4 | exp4 DIFOP exp4 | exp4 ;
exp4: exp5 LESSOP exp5 | exp5 LESSEQOP exp5 | exp5 GRTOP exp5 | exp5 GRTEQOP exp5 | exp5;
exp5: exp5 ADDOP exp6 | exp5 SUBOP exp6 | exp6 ;
exp6: exp6 DIVOP exp7 | exp6 MULOP exp7 | exp6 MODOP exp7 | exp7 ;
exp7: SUBOP exp7 | NOTOP exp7 | exp8 ;
exp8: exp8 LSB exp RSB | exp9 ;
exp9: LB exp RB | operand ;
operand: INTLIT | STRINGLIT | FLOATLIT | BOOLLIT | ID | funcall ;

//function call
funcall: ID LB (exp (COMMA exp)*)? RB ;
//explist: expfunc (COMMA expfunc)* ;
//expfunc: INTLIT | STRINGLIT | FLOATLIT | BOOLLIT | ID | exp;
primetype: BOOLTYPE | INTTYPE | FLOATTYPE | STRTYPE ;
BOOLLIT: TRUE | FALSE ;
//keywords
INTTYPE: 'int' ;
VOIDTYPE: 'void' ;
BOOLTYPE: 'boolean';
STRTYPE: 'string';
FLOATTYPE: 'float';
BREAK: 'break';
CONTINUE: 'continue';
ELSE: 'else';
IF: 'if';
FOR: 'for';
RETURN: 'return';
DO: 'do';
WHILE: 'while';
TRUE: 'true' ;
FALSE: 'false' ;



fragment Letter: [a-zA-Z];
fragment Digit: [0-9];
fragment Underscore: '_';

ID: (Letter | Underscore) (Letter | Digit | Underscore)*;

//literals
INTLIT: Digit+;
FLOATLIT: Digit* Dot Digit+ (('e' | 'E') '-'? Digit+)? | Digit+ Dot Digit* (('e' | 'E') '-'? Digit+)? | Digit+ ('e' | 'E') '-'? Digit+ ;

STRINGLIT: '"' ('\\' [bfnrt"\\] | ~[\b\f\n\r\t"\\])* '"'{
    self.text = self.text[1:-1]
};

LB: '(' ;
RB: ')' ;
LP: '{';
RP: '}';
LSB: '[';
RSB: ']';
SEMI: ';' ;
COMMA: ',';

WHITESPACE_CHAR: [ \f\t\r\n]+ -> skip ;

COMMENT_BLOCK: '/*' .*? '*/' ->skip ;

COMMENT_LINE: '//' .*? ('\n' | '\r' | EOF) ->skip ;


fragment Dot: '.';
fragment Exponent: ('e') ('-') Digit ;

//OPERATOR
ADDOP: '+';
SUBOP: '-';
MULOP: '*';
DIVOP: '/';
NOTOP: '!';
MODOP: '%';
OROP: '||';
ANDOP: '&&';
DIFOP: '!=';
EQOP: '==';
LESSOP: '<';
GRTOP: '>';
LESSEQOP: '<=';
GRTEQOP: '>=';
ASSOP: '=';


UNCLOSE_STRING: '"' ('\\' [bfnrt"\\] | ~[\b\f\n\r\t"\\])*{
    raise UncloseString(self.text[1:])
};

ILLEGAL_ESCAPE: '"' ('\\' [bfnrt"\\] | ~[\b\f\n\r\t"\\])* ('\\' ~[bfnrt"\\] | [\b\f\t"\\]) {
    raise IllegalEscape(self.text[1:])
};

ERROR_CHAR: .{
    raise ErrorToken(self.text)
};
