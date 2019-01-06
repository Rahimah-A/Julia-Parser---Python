from enum import Enum


class TokenType(Enum):
    FUNCTION_TOK = 1
    LEFT_PAREN_TOK =2
    RIGHT_PAREN_TOK = 3
    IF_TOK = 4
    THEN_TOK = 5
    END_TOK = 6
    ELSE_TOK = 7
    WHILE_TOK = 8
    DO_TOK = 9
    ID_TOK = 10
    PRINT_TOK = 11
    GE_TOK = 12
    GT_TOK = 13
    REPEAT_TOK = 14
    UNTIL_TOK = 15
    LE_TOK = 16
    LT_TOK = 17
    EQ_TOK = 18
    NE_TOK = 19
    ADD_TOK = 20
    SUB_TOK = 21
    MUL_TOK = 22
    DIV_TOK = 23
    ASSIGN_TOK = 24
    EOS_TOK = 25
    LITERAL_INTEGER_TOK = 26
    MOD_TOK = 27
    EXP_TOK = 28
    REV_DIV_TOK = 29
    COL_TOK = 30
    FOR_TOK = 31
