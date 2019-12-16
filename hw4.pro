c:-['family.pro'].

% facts

male('King Gorge VI').
male('Charles Prince of Wales').
male('Andrew Duke of York').
male('Edward Earl of Wessex').
male('David Viscount Linley').
male('Prince William of Wales').
male('Prince Harry of Wales').
male('Peter Phillips').
male('James Viscount Severn').
male('Charles Armstrong Jones').
male('Samuel Chatto').
male('Arthur Chatto').

female('Queen Elizabeth II').
female('Princess Magaret').
female('Princess Anne').
female('Lady Sara Chatto').
female('Zara Tindall').
female('Princess Beatrice of York').
female('Princess Eugenle of York').
female('Savannah Phillips').
female('Isla Phillips').
female('Lady Louise Windsor').
female('Magarita Armstrong Jones').

parent_of('Savannah Phillips','Peter Phillips').
parent_of('Isla Phillips','Peter Phillips').
parent_of('Lady Louise Windsor','Edward Earl of Wessex').
parent_of('James Viscount Severn','Edward Earl of Wessex').
parent_of('Princess Eugenle of York','Andrew Duke of York').
parent_of('Princess Beatrice of York','Andrew Duke of York').
parent_of('Peter Phillips','Princess Anne').
parent_of('Zara Tindall','Princess Anne').
parent_of('Prince Harry of Wales','Charles Prince of Wales').
parent_of('Prince William of Wales','Charles Prince of Wales').
parent_of('Arthur Chatto','Lady Sara Chatto').
parent_of('Samuel Chatto','Lady Sara Chatto').
parent_of('Magarita Armstrong Jones','David Viscount Linley').
parent_of('Charles Armstrong Jones','David Viscount Linley').
parent_of('Edward Earl of Wessex','Queen Elizabeth II').
parent_of('Andrew Duke of York','Queen Elizabeth II').
parent_of('Princess Anne','Queen Elizabeth II').
parent_of('Charles Prince of Wales','Queen Elizabeth II').
parent_of('David Viscount Linley','Princess Magaret').
parent_of('Lady Sara Chatto','Princess Magaret').
parent_of('Queen Elizabeth II','King Gorge VI').
parent_of('Princess Magaret','King Gorge VI').





% rules
sibling_of(X,S):-parent_of(X,P),parent_of(S,P),X\==S.

brother_of(X,B):-sibling_of(X,B),male(B).

sister_of(X,S):-sibling_of(X,S),female(S).

mother_of(X,M):-parent_of(X,M),female(M).

father_of(X,M):-parent_of(X,M),male(M).

gp_of(X,GP):-parent_of(X,P),parent_of(P,GP).

cousin_of(X,C):-
  gp_of(X,GP),
  gp_of(C,GP),
  X\==C,
  not(sibling_of(X,C)).

uncle_or_aunt_of(X,Who):-
  parent_of(X,P),
  sibling_of(P,Who).

uncle_of(X,Who):-uncle_or_aunt_of(X,Who),male(Who).

aunt_of(X,Who):-uncle_or_aunt_of(X,Who),female(Who).



ancestor_of(X,Z):-parent_of(X,Z).
ancestor_of(X,Z):-parent_of(X,Y),ancestor_of(Y,Z).
