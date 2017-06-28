rpn(InputList) -> rpn(InputList, []).
rpn([], Stack) -> Stack;
rpn([X | InputTail], Stack) when is_number(X) ->
  rpn(InputTail, [X | Stack]);
rpn(['+' | InputTail], [V2, V1 | StackTail]) -> 
  rpn(InputTail, [V1 + V2 | StackTail]);
rpn(['-' | InputTail], [V2, V1 | StackTail]) -> 
  rpn(InputTail, [V1 - V2 | StackTail]);
rpn(['*' | InputTail], [V2, V1 | StackTail]) -> 
  rpn(InputTail, [V1 * V2 | StackTail]);
rpn(['/' | InputTail], [V2, V1 | StackTail]) when V2 /= 0 ->
  rpn(InputTail, [V1 / V2 | StackTail]);
rpn(['/' | _], [V2 | _]) when V2 == 0 ->
  rpn_error_divide_by_zero;
rpn(['p' | InputTail], Stack = [V | _]) ->
  io:format("~w~n", [V]),
  rpn(InputTail, Stack);
rpn(['P' | InputTail], Stack) ->
  io:format("~w~n", [Stack]),
  rpn(InputTail, Stack);
rpn([A | _], _) when is_atom(A) ->
  case lists:member(A, ['+', '-', '*', '/', 'p', 'P']) of
    true  -> rpn_error_stack_underflow;
    false -> rpn_error_unrecognized_operator
  end;
rpn(_, _) -> rpn_error_invalid_input_element.

rpn_fold(InputList) ->
  element(1, lists:foldl(
    fun(X, {Stack, Pos}) ->
      Oops = fun(Msg) -> % report an error
	io:format("~s at input position ~b.~n", [Msg, Pos]),
	rpn_error
      end,
      { case {X, Stack} of % update the stack
	  {_, rpn_error} -> rpn_error;
	  _ when is_number(X) -> [X | Stack];
	  {'+', [V2, V1 | StackTail]} ->  [V1 + V2 | StackTail];
	  {'-', [V2, V1 | StackTail]} ->  [V1 - V2 | StackTail];
	  {'*', [V2, V1 | StackTail]} ->  [V1 * V2 | StackTail];
	  {'/', [V2, V1 | StackTail]} when V2 /= 0 -> [V1 / V2 | StackTail];
	  {'/', [V | _]} when V == 0 -> Oops("Divide by zero");
	  {'p', Stack = [V | _]} ->
	    io:format("~w~n", [V]),
	    Stack;
	  {'P', Stack} ->
	    io:format("~w~n", [Stack]),
	    Stack;
	  _ ->
	    IsOp = is_atom(X) andalso lists:member(X, ['+', '-', '*', '/', 'p', 'P']),
	    Oops(if
	      IsOp -> "Stack underflow";
	      is_atom(X) -> "Unrecognized operator";
	      true -> "Number or operator expected"
	    end)
        end,
	Pos+1 % update pos
      }
    end,
    {[], 1}, InputList)).