# Generated from main/mc/parser/MC.g4 by ANTLR 4.7.2
from antlr4 import *
from io import StringIO
from typing.io import TextIO
import sys


from lexererr import *



def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2\63")
        buf.write("\u01a3\b\1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7")
        buf.write("\t\7\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r")
        buf.write("\4\16\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4\23")
        buf.write("\t\23\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30")
        buf.write("\4\31\t\31\4\32\t\32\4\33\t\33\4\34\t\34\4\35\t\35\4\36")
        buf.write("\t\36\4\37\t\37\4 \t \4!\t!\4\"\t\"\4#\t#\4$\t$\4%\t%")
        buf.write("\4&\t&\4\'\t\'\4(\t(\4)\t)\4*\t*\4+\t+\4,\t,\4-\t-\4.")
        buf.write("\t.\4/\t/\4\60\t\60\4\61\t\61\4\62\t\62\4\63\t\63\4\64")
        buf.write("\t\64\4\65\t\65\4\66\t\66\4\67\t\67\3\2\3\2\5\2r\n\2\3")
        buf.write("\3\3\3\3\3\3\3\3\4\3\4\3\4\3\4\3\4\3\5\3\5\3\5\3\5\3\5")
        buf.write("\3\5\3\5\3\5\3\6\3\6\3\6\3\6\3\6\3\6\3\6\3\7\3\7\3\7\3")
        buf.write("\7\3\7\3\7\3\b\3\b\3\b\3\b\3\b\3\b\3\t\3\t\3\t\3\t\3\t")
        buf.write("\3\t\3\t\3\t\3\t\3\n\3\n\3\n\3\n\3\n\3\13\3\13\3\13\3")
        buf.write("\f\3\f\3\f\3\f\3\r\3\r\3\r\3\r\3\r\3\r\3\r\3\16\3\16\3")
        buf.write("\16\3\17\3\17\3\17\3\17\3\17\3\17\3\20\3\20\3\20\3\20")
        buf.write("\3\20\3\21\3\21\3\21\3\21\3\21\3\21\3\22\3\22\3\23\3\23")
        buf.write("\3\24\3\24\3\25\3\25\5\25\u00d0\n\25\3\25\3\25\3\25\7")
        buf.write("\25\u00d5\n\25\f\25\16\25\u00d8\13\25\3\26\6\26\u00db")
        buf.write("\n\26\r\26\16\26\u00dc\3\27\7\27\u00e0\n\27\f\27\16\27")
        buf.write("\u00e3\13\27\3\27\3\27\6\27\u00e7\n\27\r\27\16\27\u00e8")
        buf.write("\3\27\3\27\5\27\u00ed\n\27\3\27\6\27\u00f0\n\27\r\27\16")
        buf.write("\27\u00f1\5\27\u00f4\n\27\3\27\6\27\u00f7\n\27\r\27\16")
        buf.write("\27\u00f8\3\27\3\27\7\27\u00fd\n\27\f\27\16\27\u0100\13")
        buf.write("\27\3\27\3\27\5\27\u0104\n\27\3\27\6\27\u0107\n\27\r\27")
        buf.write("\16\27\u0108\5\27\u010b\n\27\3\27\6\27\u010e\n\27\r\27")
        buf.write("\16\27\u010f\3\27\3\27\5\27\u0114\n\27\3\27\6\27\u0117")
        buf.write("\n\27\r\27\16\27\u0118\5\27\u011b\n\27\3\30\3\30\3\30")
        buf.write("\3\30\7\30\u0121\n\30\f\30\16\30\u0124\13\30\3\30\3\30")
        buf.write("\3\30\3\31\3\31\3\32\3\32\3\33\3\33\3\34\3\34\3\35\3\35")
        buf.write("\3\36\3\36\3\37\3\37\3 \3 \3!\6!\u013a\n!\r!\16!\u013b")
        buf.write("\3!\3!\3\"\3\"\3\"\3\"\7\"\u0144\n\"\f\"\16\"\u0147\13")
        buf.write("\"\3\"\3\"\3\"\3\"\3\"\3#\3#\3#\3#\7#\u0152\n#\f#\16#")
        buf.write("\u0155\13#\3#\5#\u0158\n#\3#\3#\3$\3$\3%\3%\3%\3%\3&\3")
        buf.write("&\3\'\3\'\3(\3(\3)\3)\3*\3*\3+\3+\3,\3,\3,\3-\3-\3-\3")
        buf.write(".\3.\3.\3/\3/\3/\3\60\3\60\3\61\3\61\3\62\3\62\3\62\3")
        buf.write("\63\3\63\3\63\3\64\3\64\3\65\3\65\3\65\3\65\7\65\u018a")
        buf.write("\n\65\f\65\16\65\u018d\13\65\3\65\3\65\3\66\3\66\3\66")
        buf.write("\3\66\7\66\u0195\n\66\f\66\16\66\u0198\13\66\3\66\3\66")
        buf.write("\3\66\5\66\u019d\n\66\3\66\3\66\3\67\3\67\3\67\4\u0145")
        buf.write("\u0153\28\3\3\5\4\7\5\t\6\13\7\r\b\17\t\21\n\23\13\25")
        buf.write("\f\27\r\31\16\33\17\35\20\37\21!\22#\2%\2\'\2)\23+\24")
        buf.write("-\25/\26\61\27\63\30\65\31\67\329\33;\34=\35?\36A\37C")
        buf.write(" E!G\2I\2K\"M#O$Q%S&U\'W(Y)[*]+_,a-c.e/g\60i\61k\62m\63")
        buf.write("\3\2\n\4\2C\\c|\3\2\62;\4\2GGgg\t\2$$^^ddhhppttvv\6\2")
        buf.write("\n\f\16\17$$^^\5\2\13\f\16\17\"\"\4\3\f\f\17\17\6\2\n")
        buf.write("\13\16\16$$^^\2\u01bc\2\3\3\2\2\2\2\5\3\2\2\2\2\7\3\2")
        buf.write("\2\2\2\t\3\2\2\2\2\13\3\2\2\2\2\r\3\2\2\2\2\17\3\2\2\2")
        buf.write("\2\21\3\2\2\2\2\23\3\2\2\2\2\25\3\2\2\2\2\27\3\2\2\2\2")
        buf.write("\31\3\2\2\2\2\33\3\2\2\2\2\35\3\2\2\2\2\37\3\2\2\2\2!")
        buf.write("\3\2\2\2\2)\3\2\2\2\2+\3\2\2\2\2-\3\2\2\2\2/\3\2\2\2\2")
        buf.write("\61\3\2\2\2\2\63\3\2\2\2\2\65\3\2\2\2\2\67\3\2\2\2\29")
        buf.write("\3\2\2\2\2;\3\2\2\2\2=\3\2\2\2\2?\3\2\2\2\2A\3\2\2\2\2")
        buf.write("C\3\2\2\2\2E\3\2\2\2\2K\3\2\2\2\2M\3\2\2\2\2O\3\2\2\2")
        buf.write("\2Q\3\2\2\2\2S\3\2\2\2\2U\3\2\2\2\2W\3\2\2\2\2Y\3\2\2")
        buf.write("\2\2[\3\2\2\2\2]\3\2\2\2\2_\3\2\2\2\2a\3\2\2\2\2c\3\2")
        buf.write("\2\2\2e\3\2\2\2\2g\3\2\2\2\2i\3\2\2\2\2k\3\2\2\2\2m\3")
        buf.write("\2\2\2\3q\3\2\2\2\5s\3\2\2\2\7w\3\2\2\2\t|\3\2\2\2\13")
        buf.write("\u0084\3\2\2\2\r\u008b\3\2\2\2\17\u0091\3\2\2\2\21\u0097")
        buf.write("\3\2\2\2\23\u00a0\3\2\2\2\25\u00a5\3\2\2\2\27\u00a8\3")
        buf.write("\2\2\2\31\u00ac\3\2\2\2\33\u00b3\3\2\2\2\35\u00b6\3\2")
        buf.write("\2\2\37\u00bc\3\2\2\2!\u00c1\3\2\2\2#\u00c7\3\2\2\2%\u00c9")
        buf.write("\3\2\2\2\'\u00cb\3\2\2\2)\u00cf\3\2\2\2+\u00da\3\2\2\2")
        buf.write("-\u011a\3\2\2\2/\u011c\3\2\2\2\61\u0128\3\2\2\2\63\u012a")
        buf.write("\3\2\2\2\65\u012c\3\2\2\2\67\u012e\3\2\2\29\u0130\3\2")
        buf.write("\2\2;\u0132\3\2\2\2=\u0134\3\2\2\2?\u0136\3\2\2\2A\u0139")
        buf.write("\3\2\2\2C\u013f\3\2\2\2E\u014d\3\2\2\2G\u015b\3\2\2\2")
        buf.write("I\u015d\3\2\2\2K\u0161\3\2\2\2M\u0163\3\2\2\2O\u0165\3")
        buf.write("\2\2\2Q\u0167\3\2\2\2S\u0169\3\2\2\2U\u016b\3\2\2\2W\u016d")
        buf.write("\3\2\2\2Y\u0170\3\2\2\2[\u0173\3\2\2\2]\u0176\3\2\2\2")
        buf.write("_\u0179\3\2\2\2a\u017b\3\2\2\2c\u017d\3\2\2\2e\u0180\3")
        buf.write("\2\2\2g\u0183\3\2\2\2i\u0185\3\2\2\2k\u0190\3\2\2\2m\u01a0")
        buf.write("\3\2\2\2or\5\37\20\2pr\5!\21\2qo\3\2\2\2qp\3\2\2\2r\4")
        buf.write("\3\2\2\2st\7k\2\2tu\7p\2\2uv\7v\2\2v\6\3\2\2\2wx\7x\2")
        buf.write("\2xy\7q\2\2yz\7k\2\2z{\7f\2\2{\b\3\2\2\2|}\7d\2\2}~\7")
        buf.write("q\2\2~\177\7q\2\2\177\u0080\7n\2\2\u0080\u0081\7g\2\2")
        buf.write("\u0081\u0082\7c\2\2\u0082\u0083\7p\2\2\u0083\n\3\2\2\2")
        buf.write("\u0084\u0085\7u\2\2\u0085\u0086\7v\2\2\u0086\u0087\7t")
        buf.write("\2\2\u0087\u0088\7k\2\2\u0088\u0089\7p\2\2\u0089\u008a")
        buf.write("\7i\2\2\u008a\f\3\2\2\2\u008b\u008c\7h\2\2\u008c\u008d")
        buf.write("\7n\2\2\u008d\u008e\7q\2\2\u008e\u008f\7c\2\2\u008f\u0090")
        buf.write("\7v\2\2\u0090\16\3\2\2\2\u0091\u0092\7d\2\2\u0092\u0093")
        buf.write("\7t\2\2\u0093\u0094\7g\2\2\u0094\u0095\7c\2\2\u0095\u0096")
        buf.write("\7m\2\2\u0096\20\3\2\2\2\u0097\u0098\7e\2\2\u0098\u0099")
        buf.write("\7q\2\2\u0099\u009a\7p\2\2\u009a\u009b\7v\2\2\u009b\u009c")
        buf.write("\7k\2\2\u009c\u009d\7p\2\2\u009d\u009e\7w\2\2\u009e\u009f")
        buf.write("\7g\2\2\u009f\22\3\2\2\2\u00a0\u00a1\7g\2\2\u00a1\u00a2")
        buf.write("\7n\2\2\u00a2\u00a3\7u\2\2\u00a3\u00a4\7g\2\2\u00a4\24")
        buf.write("\3\2\2\2\u00a5\u00a6\7k\2\2\u00a6\u00a7\7h\2\2\u00a7\26")
        buf.write("\3\2\2\2\u00a8\u00a9\7h\2\2\u00a9\u00aa\7q\2\2\u00aa\u00ab")
        buf.write("\7t\2\2\u00ab\30\3\2\2\2\u00ac\u00ad\7t\2\2\u00ad\u00ae")
        buf.write("\7g\2\2\u00ae\u00af\7v\2\2\u00af\u00b0\7w\2\2\u00b0\u00b1")
        buf.write("\7t\2\2\u00b1\u00b2\7p\2\2\u00b2\32\3\2\2\2\u00b3\u00b4")
        buf.write("\7f\2\2\u00b4\u00b5\7q\2\2\u00b5\34\3\2\2\2\u00b6\u00b7")
        buf.write("\7y\2\2\u00b7\u00b8\7j\2\2\u00b8\u00b9\7k\2\2\u00b9\u00ba")
        buf.write("\7n\2\2\u00ba\u00bb\7g\2\2\u00bb\36\3\2\2\2\u00bc\u00bd")
        buf.write("\7v\2\2\u00bd\u00be\7t\2\2\u00be\u00bf\7w\2\2\u00bf\u00c0")
        buf.write("\7g\2\2\u00c0 \3\2\2\2\u00c1\u00c2\7h\2\2\u00c2\u00c3")
        buf.write("\7c\2\2\u00c3\u00c4\7n\2\2\u00c4\u00c5\7u\2\2\u00c5\u00c6")
        buf.write("\7g\2\2\u00c6\"\3\2\2\2\u00c7\u00c8\t\2\2\2\u00c8$\3\2")
        buf.write("\2\2\u00c9\u00ca\t\3\2\2\u00ca&\3\2\2\2\u00cb\u00cc\7")
        buf.write("a\2\2\u00cc(\3\2\2\2\u00cd\u00d0\5#\22\2\u00ce\u00d0\5")
        buf.write("\'\24\2\u00cf\u00cd\3\2\2\2\u00cf\u00ce\3\2\2\2\u00d0")
        buf.write("\u00d6\3\2\2\2\u00d1\u00d5\5#\22\2\u00d2\u00d5\5%\23\2")
        buf.write("\u00d3\u00d5\5\'\24\2\u00d4\u00d1\3\2\2\2\u00d4\u00d2")
        buf.write("\3\2\2\2\u00d4\u00d3\3\2\2\2\u00d5\u00d8\3\2\2\2\u00d6")
        buf.write("\u00d4\3\2\2\2\u00d6\u00d7\3\2\2\2\u00d7*\3\2\2\2\u00d8")
        buf.write("\u00d6\3\2\2\2\u00d9\u00db\5%\23\2\u00da\u00d9\3\2\2\2")
        buf.write("\u00db\u00dc\3\2\2\2\u00dc\u00da\3\2\2\2\u00dc\u00dd\3")
        buf.write("\2\2\2\u00dd,\3\2\2\2\u00de\u00e0\5%\23\2\u00df\u00de")
        buf.write("\3\2\2\2\u00e0\u00e3\3\2\2\2\u00e1\u00df\3\2\2\2\u00e1")
        buf.write("\u00e2\3\2\2\2\u00e2\u00e4\3\2\2\2\u00e3\u00e1\3\2\2\2")
        buf.write("\u00e4\u00e6\5G$\2\u00e5\u00e7\5%\23\2\u00e6\u00e5\3\2")
        buf.write("\2\2\u00e7\u00e8\3\2\2\2\u00e8\u00e6\3\2\2\2\u00e8\u00e9")
        buf.write("\3\2\2\2\u00e9\u00f3\3\2\2\2\u00ea\u00ec\t\4\2\2\u00eb")
        buf.write("\u00ed\7/\2\2\u00ec\u00eb\3\2\2\2\u00ec\u00ed\3\2\2\2")
        buf.write("\u00ed\u00ef\3\2\2\2\u00ee\u00f0\5%\23\2\u00ef\u00ee\3")
        buf.write("\2\2\2\u00f0\u00f1\3\2\2\2\u00f1\u00ef\3\2\2\2\u00f1\u00f2")
        buf.write("\3\2\2\2\u00f2\u00f4\3\2\2\2\u00f3\u00ea\3\2\2\2\u00f3")
        buf.write("\u00f4\3\2\2\2\u00f4\u011b\3\2\2\2\u00f5\u00f7\5%\23\2")
        buf.write("\u00f6\u00f5\3\2\2\2\u00f7\u00f8\3\2\2\2\u00f8\u00f6\3")
        buf.write("\2\2\2\u00f8\u00f9\3\2\2\2\u00f9\u00fa\3\2\2\2\u00fa\u00fe")
        buf.write("\5G$\2\u00fb\u00fd\5%\23\2\u00fc\u00fb\3\2\2\2\u00fd\u0100")
        buf.write("\3\2\2\2\u00fe\u00fc\3\2\2\2\u00fe\u00ff\3\2\2\2\u00ff")
        buf.write("\u010a\3\2\2\2\u0100\u00fe\3\2\2\2\u0101\u0103\t\4\2\2")
        buf.write("\u0102\u0104\7/\2\2\u0103\u0102\3\2\2\2\u0103\u0104\3")
        buf.write("\2\2\2\u0104\u0106\3\2\2\2\u0105\u0107\5%\23\2\u0106\u0105")
        buf.write("\3\2\2\2\u0107\u0108\3\2\2\2\u0108\u0106\3\2\2\2\u0108")
        buf.write("\u0109\3\2\2\2\u0109\u010b\3\2\2\2\u010a\u0101\3\2\2\2")
        buf.write("\u010a\u010b\3\2\2\2\u010b\u011b\3\2\2\2\u010c\u010e\5")
        buf.write("%\23\2\u010d\u010c\3\2\2\2\u010e\u010f\3\2\2\2\u010f\u010d")
        buf.write("\3\2\2\2\u010f\u0110\3\2\2\2\u0110\u0111\3\2\2\2\u0111")
        buf.write("\u0113\t\4\2\2\u0112\u0114\7/\2\2\u0113\u0112\3\2\2\2")
        buf.write("\u0113\u0114\3\2\2\2\u0114\u0116\3\2\2\2\u0115\u0117\5")
        buf.write("%\23\2\u0116\u0115\3\2\2\2\u0117\u0118\3\2\2\2\u0118\u0116")
        buf.write("\3\2\2\2\u0118\u0119\3\2\2\2\u0119\u011b\3\2\2\2\u011a")
        buf.write("\u00e1\3\2\2\2\u011a\u00f6\3\2\2\2\u011a\u010d\3\2\2\2")
        buf.write("\u011b.\3\2\2\2\u011c\u0122\7$\2\2\u011d\u011e\7^\2\2")
        buf.write("\u011e\u0121\t\5\2\2\u011f\u0121\n\6\2\2\u0120\u011d\3")
        buf.write("\2\2\2\u0120\u011f\3\2\2\2\u0121\u0124\3\2\2\2\u0122\u0120")
        buf.write("\3\2\2\2\u0122\u0123\3\2\2\2\u0123\u0125\3\2\2\2\u0124")
        buf.write("\u0122\3\2\2\2\u0125\u0126\7$\2\2\u0126\u0127\b\30\2\2")
        buf.write("\u0127\60\3\2\2\2\u0128\u0129\7*\2\2\u0129\62\3\2\2\2")
        buf.write("\u012a\u012b\7+\2\2\u012b\64\3\2\2\2\u012c\u012d\7}\2")
        buf.write("\2\u012d\66\3\2\2\2\u012e\u012f\7\177\2\2\u012f8\3\2\2")
        buf.write("\2\u0130\u0131\7]\2\2\u0131:\3\2\2\2\u0132\u0133\7_\2")
        buf.write("\2\u0133<\3\2\2\2\u0134\u0135\7=\2\2\u0135>\3\2\2\2\u0136")
        buf.write("\u0137\7.\2\2\u0137@\3\2\2\2\u0138\u013a\t\7\2\2\u0139")
        buf.write("\u0138\3\2\2\2\u013a\u013b\3\2\2\2\u013b\u0139\3\2\2\2")
        buf.write("\u013b\u013c\3\2\2\2\u013c\u013d\3\2\2\2\u013d\u013e\b")
        buf.write("!\3\2\u013eB\3\2\2\2\u013f\u0140\7\61\2\2\u0140\u0141")
        buf.write("\7,\2\2\u0141\u0145\3\2\2\2\u0142\u0144\13\2\2\2\u0143")
        buf.write("\u0142\3\2\2\2\u0144\u0147\3\2\2\2\u0145\u0146\3\2\2\2")
        buf.write("\u0145\u0143\3\2\2\2\u0146\u0148\3\2\2\2\u0147\u0145\3")
        buf.write("\2\2\2\u0148\u0149\7,\2\2\u0149\u014a\7\61\2\2\u014a\u014b")
        buf.write("\3\2\2\2\u014b\u014c\b\"\3\2\u014cD\3\2\2\2\u014d\u014e")
        buf.write("\7\61\2\2\u014e\u014f\7\61\2\2\u014f\u0153\3\2\2\2\u0150")
        buf.write("\u0152\13\2\2\2\u0151\u0150\3\2\2\2\u0152\u0155\3\2\2")
        buf.write("\2\u0153\u0154\3\2\2\2\u0153\u0151\3\2\2\2\u0154\u0157")
        buf.write("\3\2\2\2\u0155\u0153\3\2\2\2\u0156\u0158\t\b\2\2\u0157")
        buf.write("\u0156\3\2\2\2\u0158\u0159\3\2\2\2\u0159\u015a\b#\3\2")
        buf.write("\u015aF\3\2\2\2\u015b\u015c\7\60\2\2\u015cH\3\2\2\2\u015d")
        buf.write("\u015e\7g\2\2\u015e\u015f\7/\2\2\u015f\u0160\5%\23\2\u0160")
        buf.write("J\3\2\2\2\u0161\u0162\7-\2\2\u0162L\3\2\2\2\u0163\u0164")
        buf.write("\7/\2\2\u0164N\3\2\2\2\u0165\u0166\7,\2\2\u0166P\3\2\2")
        buf.write("\2\u0167\u0168\7\61\2\2\u0168R\3\2\2\2\u0169\u016a\7#")
        buf.write("\2\2\u016aT\3\2\2\2\u016b\u016c\7\'\2\2\u016cV\3\2\2\2")
        buf.write("\u016d\u016e\7~\2\2\u016e\u016f\7~\2\2\u016fX\3\2\2\2")
        buf.write("\u0170\u0171\7(\2\2\u0171\u0172\7(\2\2\u0172Z\3\2\2\2")
        buf.write("\u0173\u0174\7#\2\2\u0174\u0175\7?\2\2\u0175\\\3\2\2\2")
        buf.write("\u0176\u0177\7?\2\2\u0177\u0178\7?\2\2\u0178^\3\2\2\2")
        buf.write("\u0179\u017a\7>\2\2\u017a`\3\2\2\2\u017b\u017c\7@\2\2")
        buf.write("\u017cb\3\2\2\2\u017d\u017e\7>\2\2\u017e\u017f\7?\2\2")
        buf.write("\u017fd\3\2\2\2\u0180\u0181\7@\2\2\u0181\u0182\7?\2\2")
        buf.write("\u0182f\3\2\2\2\u0183\u0184\7?\2\2\u0184h\3\2\2\2\u0185")
        buf.write("\u018b\7$\2\2\u0186\u0187\7^\2\2\u0187\u018a\t\5\2\2\u0188")
        buf.write("\u018a\n\6\2\2\u0189\u0186\3\2\2\2\u0189\u0188\3\2\2\2")
        buf.write("\u018a\u018d\3\2\2\2\u018b\u0189\3\2\2\2\u018b\u018c\3")
        buf.write("\2\2\2\u018c\u018e\3\2\2\2\u018d\u018b\3\2\2\2\u018e\u018f")
        buf.write("\b\65\4\2\u018fj\3\2\2\2\u0190\u0196\7$\2\2\u0191\u0192")
        buf.write("\7^\2\2\u0192\u0195\t\5\2\2\u0193\u0195\n\6\2\2\u0194")
        buf.write("\u0191\3\2\2\2\u0194\u0193\3\2\2\2\u0195\u0198\3\2\2\2")
        buf.write("\u0196\u0194\3\2\2\2\u0196\u0197\3\2\2\2\u0197\u019c\3")
        buf.write("\2\2\2\u0198\u0196\3\2\2\2\u0199\u019a\7^\2\2\u019a\u019d")
        buf.write("\n\5\2\2\u019b\u019d\t\t\2\2\u019c\u0199\3\2\2\2\u019c")
        buf.write("\u019b\3\2\2\2\u019d\u019e\3\2\2\2\u019e\u019f\b\66\5")
        buf.write("\2\u019fl\3\2\2\2\u01a0\u01a1\13\2\2\2\u01a1\u01a2\b\67")
        buf.write("\6\2\u01a2n\3\2\2\2!\2q\u00cf\u00d4\u00d6\u00dc\u00e1")
        buf.write("\u00e8\u00ec\u00f1\u00f3\u00f8\u00fe\u0103\u0108\u010a")
        buf.write("\u010f\u0113\u0118\u011a\u0120\u0122\u013b\u0145\u0153")
        buf.write("\u0157\u0189\u018b\u0194\u0196\u019c\7\3\30\2\b\2\2\3")
        buf.write("\65\3\3\66\4\3\67\5")
        return buf.getvalue()


class MCLexer(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    BOOLLIT = 1
    INTTYPE = 2
    VOIDTYPE = 3
    BOOLTYPE = 4
    STRTYPE = 5
    FLOATTYPE = 6
    BREAK = 7
    CONTINUE = 8
    ELSE = 9
    IF = 10
    FOR = 11
    RETURN = 12
    DO = 13
    WHILE = 14
    TRUE = 15
    FALSE = 16
    ID = 17
    INTLIT = 18
    FLOATLIT = 19
    STRINGLIT = 20
    LB = 21
    RB = 22
    LP = 23
    RP = 24
    LSB = 25
    RSB = 26
    SEMI = 27
    COMMA = 28
    WHITESPACE_CHAR = 29
    COMMENT_BLOCK = 30
    COMMENT_LINE = 31
    ADDOP = 32
    SUBOP = 33
    MULOP = 34
    DIVOP = 35
    NOTOP = 36
    MODOP = 37
    OROP = 38
    ANDOP = 39
    DIFOP = 40
    EQOP = 41
    LESSOP = 42
    GRTOP = 43
    LESSEQOP = 44
    GRTEQOP = 45
    ASSOP = 46
    UNCLOSE_STRING = 47
    ILLEGAL_ESCAPE = 48
    ERROR_CHAR = 49

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "'int'", "'void'", "'boolean'", "'string'", "'float'", "'break'", 
            "'continue'", "'else'", "'if'", "'for'", "'return'", "'do'", 
            "'while'", "'true'", "'false'", "'('", "')'", "'{'", "'}'", 
            "'['", "']'", "';'", "','", "'+'", "'-'", "'*'", "'/'", "'!'", 
            "'%'", "'||'", "'&&'", "'!='", "'=='", "'<'", "'>'", "'<='", 
            "'>='", "'='" ]

    symbolicNames = [ "<INVALID>",
            "BOOLLIT", "INTTYPE", "VOIDTYPE", "BOOLTYPE", "STRTYPE", "FLOATTYPE", 
            "BREAK", "CONTINUE", "ELSE", "IF", "FOR", "RETURN", "DO", "WHILE", 
            "TRUE", "FALSE", "ID", "INTLIT", "FLOATLIT", "STRINGLIT", "LB", 
            "RB", "LP", "RP", "LSB", "RSB", "SEMI", "COMMA", "WHITESPACE_CHAR", 
            "COMMENT_BLOCK", "COMMENT_LINE", "ADDOP", "SUBOP", "MULOP", 
            "DIVOP", "NOTOP", "MODOP", "OROP", "ANDOP", "DIFOP", "EQOP", 
            "LESSOP", "GRTOP", "LESSEQOP", "GRTEQOP", "ASSOP", "UNCLOSE_STRING", 
            "ILLEGAL_ESCAPE", "ERROR_CHAR" ]

    ruleNames = [ "BOOLLIT", "INTTYPE", "VOIDTYPE", "BOOLTYPE", "STRTYPE", 
                  "FLOATTYPE", "BREAK", "CONTINUE", "ELSE", "IF", "FOR", 
                  "RETURN", "DO", "WHILE", "TRUE", "FALSE", "Letter", "Digit", 
                  "Underscore", "ID", "INTLIT", "FLOATLIT", "STRINGLIT", 
                  "LB", "RB", "LP", "RP", "LSB", "RSB", "SEMI", "COMMA", 
                  "WHITESPACE_CHAR", "COMMENT_BLOCK", "COMMENT_LINE", "Dot", 
                  "Exponent", "ADDOP", "SUBOP", "MULOP", "DIVOP", "NOTOP", 
                  "MODOP", "OROP", "ANDOP", "DIFOP", "EQOP", "LESSOP", "GRTOP", 
                  "LESSEQOP", "GRTEQOP", "ASSOP", "UNCLOSE_STRING", "ILLEGAL_ESCAPE", 
                  "ERROR_CHAR" ]

    grammarFileName = "MC.g4"

    def __init__(self, input=None, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.7.2")
        self._interp = LexerATNSimulator(self, self.atn, self.decisionsToDFA, PredictionContextCache())
        self._actions = None
        self._predicates = None


    def action(self, localctx:RuleContext, ruleIndex:int, actionIndex:int):
        if self._actions is None:
            actions = dict()
            actions[22] = self.STRINGLIT_action 
            actions[51] = self.UNCLOSE_STRING_action 
            actions[52] = self.ILLEGAL_ESCAPE_action 
            actions[53] = self.ERROR_CHAR_action 
            self._actions = actions
        action = self._actions.get(ruleIndex, None)
        if action is not None:
            action(localctx, actionIndex)
        else:
            raise Exception("No registered action for:" + str(ruleIndex))


    def STRINGLIT_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 0:

                self.text = self.text[1:-1]

     

    def UNCLOSE_STRING_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 1:

                raise UncloseString(self.text[1:])

     

    def ILLEGAL_ESCAPE_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 2:

                raise IllegalEscape(self.text[1:])

     

    def ERROR_CHAR_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 3:

                raise ErrorToken(self.text)

     


