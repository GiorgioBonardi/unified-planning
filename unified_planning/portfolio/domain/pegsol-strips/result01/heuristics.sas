begin_version
3
end_version
begin_metric
1
end_metric
21
begin_variable
var0
-1
20
Atom move_ended()
Atom last_visited(pos_2_4)
Atom last_visited(pos_5_4)
Atom last_visited(pos_2_2)
Atom last_visited(pos_3_1)
Atom last_visited(pos_1_4)
Atom last_visited(pos_4_4)
Atom last_visited(pos_3_3)
Atom last_visited(pos_6_4)
Atom last_visited(pos_3_2)
Atom last_visited(pos_3_5)
Atom last_visited(pos_3_6)
Atom last_visited(pos_1_2)
Atom last_visited(pos_5_2)
Atom last_visited(pos_6_2)
Atom last_visited(pos_3_0)
Atom last_visited(pos_0_2)
Atom last_visited(pos_0_4)
Atom last_visited(pos_3_4)
Atom last_visited(pos_4_2)
end_variable
begin_variable
var1
-1
2
Atom occupied(pos_0_2)
Atom free(pos_0_2)
end_variable
begin_variable
var2
-1
2
Atom free(pos_3_3)
Atom occupied(pos_3_3)
end_variable
begin_variable
var3
-1
2
Atom occupied(pos_5_4)
Atom free(pos_5_4)
end_variable
begin_variable
var4
-1
2
Atom free(pos_4_4)
Atom occupied(pos_4_4)
end_variable
begin_variable
var5
-1
2
Atom free(pos_5_2)
Atom occupied(pos_5_2)
end_variable
begin_variable
var6
-1
2
Atom occupied(pos_6_4)
Atom free(pos_6_4)
end_variable
begin_variable
var7
-1
2
Atom free(pos_0_4)
Atom occupied(pos_0_4)
end_variable
begin_variable
var8
-1
2
Atom occupied(pos_3_1)
Atom free(pos_3_1)
end_variable
begin_variable
var9
-1
2
Atom free(pos_1_4)
Atom occupied(pos_1_4)
end_variable
begin_variable
var10
-1
2
Atom free(pos_6_2)
Atom occupied(pos_6_2)
end_variable
begin_variable
var11
-1
2
Atom occupied(pos_2_4)
Atom free(pos_2_4)
end_variable
begin_variable
var12
-1
2
Atom occupied(pos_1_3)
Atom free(pos_1_3)
end_variable
begin_variable
var13
-1
2
Atom free(pos_3_2)
Atom occupied(pos_3_2)
end_variable
begin_variable
var14
-1
2
Atom occupied(pos_3_6)
Atom free(pos_3_6)
end_variable
begin_variable
var15
-1
2
Atom free(pos_2_2)
Atom occupied(pos_2_2)
end_variable
begin_variable
var16
-1
2
Atom occupied(pos_1_2)
Atom free(pos_1_2)
end_variable
begin_variable
var17
-1
2
Atom occupied(pos_3_5)
Atom free(pos_3_5)
end_variable
begin_variable
var18
-1
2
Atom free(pos_3_0)
Atom occupied(pos_3_0)
end_variable
begin_variable
var19
-1
2
Atom occupied(pos_4_2)
Atom free(pos_4_2)
end_variable
begin_variable
var20
-1
2
Atom occupied(pos_3_4)
Atom free(pos_3_4)
end_variable
21
begin_mutex_group
2
20 1
20 0
end_mutex_group
begin_mutex_group
2
19 1
19 0
end_mutex_group
begin_mutex_group
2
18 0
18 1
end_mutex_group
begin_mutex_group
2
17 1
17 0
end_mutex_group
begin_mutex_group
2
16 1
16 0
end_mutex_group
begin_mutex_group
2
15 0
15 1
end_mutex_group
begin_mutex_group
2
14 1
14 0
end_mutex_group
begin_mutex_group
2
13 0
13 1
end_mutex_group
begin_mutex_group
2
12 1
12 0
end_mutex_group
begin_mutex_group
2
11 1
11 0
end_mutex_group
begin_mutex_group
2
10 0
10 1
end_mutex_group
begin_mutex_group
2
9 0
9 1
end_mutex_group
begin_mutex_group
2
8 1
8 0
end_mutex_group
begin_mutex_group
2
7 0
7 1
end_mutex_group
begin_mutex_group
2
6 1
6 0
end_mutex_group
begin_mutex_group
2
5 0
5 1
end_mutex_group
begin_mutex_group
20
0 16
0 17
0 12
0 5
0 3
0 1
0 15
0 4
0 9
0 7
0 18
0 10
0 11
0 19
0 6
0 13
0 2
0 14
0 8
0 0
end_mutex_group
begin_mutex_group
2
4 0
4 1
end_mutex_group
begin_mutex_group
2
3 1
3 0
end_mutex_group
begin_mutex_group
2
2 0
2 1
end_mutex_group
begin_mutex_group
2
1 1
1 0
end_mutex_group
begin_state
0
1
0
1
0
0
1
0
0
0
0
0
0
0
1
1
1
1
0
1
0
end_state
begin_goal
20
1 1
2 1
3 1
4 0
5 0
6 1
7 0
8 1
9 0
10 0
11 1
12 1
13 0
14 1
15 0
16 1
17 1
18 0
19 1
20 1
end_goal
83
begin_operator
jump_new_move pos_3_4 pos_2_4 pos_1_4
0
4
0 0 0 5
0 9 0 1
0 11 0 1
0 20 0 1
1
end_operator
begin_operator
jump_new_move pos_2_4 pos_3_4 pos_4_4
0
4
0 0 0 6
0 4 0 1
0 11 0 1
0 20 0 1
1
end_operator
begin_operator
end_move pos_1_4
0
1
0 0 5 0
0
end_operator
begin_operator
end_move pos_4_4
0
1
0 0 6 0
0
end_operator
begin_operator
jump_new_move pos_1_4 pos_1_3 pos_1_2
0
4
0 0 0 12
0 9 1 0
0 12 0 1
0 16 1 0
1
end_operator
begin_operator
jump_continue_move pos_1_4 pos_1_3 pos_1_2
0
4
0 0 5 12
0 9 1 0
0 12 0 1
0 16 1 0
0
end_operator
begin_operator
jump_continue_move pos_1_4 pos_2_4 pos_3_4
0
4
0 0 5 18
0 9 1 0
0 11 0 1
0 20 1 0
0
end_operator
begin_operator
jump_continue_move pos_4_4 pos_3_4 pos_2_4
0
4
0 0 6 1
0 4 1 0
0 11 1 0
0 20 0 1
0
end_operator
begin_operator
jump_new_move pos_2_4 pos_1_4 pos_0_4
0
4
0 0 0 17
0 7 0 1
0 9 1 0
0 11 0 1
1
end_operator
begin_operator
jump_new_move pos_3_4 pos_4_4 pos_5_4
0
4
0 0 0 2
0 3 1 0
0 4 1 0
0 20 0 1
1
end_operator
begin_operator
jump_new_move pos_1_4 pos_2_4 pos_3_4
0
4
0 0 0 18
0 9 1 0
0 11 0 1
0 20 1 0
1
end_operator
begin_operator
jump_new_move pos_4_4 pos_3_4 pos_2_4
0
4
0 0 0 1
0 4 1 0
0 11 1 0
0 20 0 1
1
end_operator
begin_operator
end_move pos_1_2
0
1
0 0 12 0
0
end_operator
begin_operator
end_move pos_3_4
0
1
0 0 18 0
0
end_operator
begin_operator
end_move pos_2_4
0
1
0 0 1 0
0
end_operator
begin_operator
end_move pos_0_4
0
1
0 0 17 0
0
end_operator
begin_operator
end_move pos_5_4
0
1
0 0 2 0
0
end_operator
begin_operator
jump_new_move pos_1_2 pos_1_3 pos_1_4
0
4
0 0 0 5
0 9 0 1
0 12 0 1
0 16 0 1
1
end_operator
begin_operator
jump_new_move pos_1_2 pos_2_2 pos_3_2
0
4
0 0 0 9
0 13 0 1
0 15 1 0
0 16 0 1
1
end_operator
begin_operator
jump_continue_move pos_1_2 pos_1_3 pos_1_4
0
4
0 0 12 5
0 9 0 1
0 12 0 1
0 16 0 1
0
end_operator
begin_operator
jump_continue_move pos_1_2 pos_2_2 pos_3_2
0
4
0 0 12 9
0 13 0 1
0 15 1 0
0 16 0 1
0
end_operator
begin_operator
jump_continue_move pos_3_4 pos_2_4 pos_1_4
0
4
0 0 18 5
0 9 0 1
0 11 0 1
0 20 0 1
0
end_operator
begin_operator
jump_continue_move pos_3_4 pos_4_4 pos_5_4
0
4
0 0 18 2
0 3 1 0
0 4 1 0
0 20 0 1
0
end_operator
begin_operator
jump_continue_move pos_2_4 pos_3_4 pos_4_4
0
4
0 0 1 6
0 4 0 1
0 11 0 1
0 20 0 1
0
end_operator
begin_operator
jump_continue_move pos_2_4 pos_1_4 pos_0_4
0
4
0 0 1 17
0 7 0 1
0 9 1 0
0 11 0 1
0
end_operator
begin_operator
jump_new_move pos_0_4 pos_1_4 pos_2_4
0
4
0 0 0 1
0 7 1 0
0 9 1 0
0 11 1 0
1
end_operator
begin_operator
jump_continue_move pos_0_4 pos_1_4 pos_2_4
0
4
0 0 17 1
0 7 1 0
0 9 1 0
0 11 1 0
0
end_operator
begin_operator
jump_new_move pos_2_2 pos_1_2 pos_0_2
0
4
0 0 0 16
0 1 1 0
0 15 1 0
0 16 0 1
1
end_operator
begin_operator
jump_new_move pos_5_4 pos_4_4 pos_3_4
0
4
0 0 0 18
0 3 0 1
0 4 1 0
0 20 1 0
1
end_operator
begin_operator
jump_continue_move pos_5_4 pos_4_4 pos_3_4
0
4
0 0 2 18
0 3 0 1
0 4 1 0
0 20 1 0
0
end_operator
begin_operator
end_move pos_3_2
0
1
0 0 9 0
0
end_operator
begin_operator
jump_new_move pos_4_4 pos_5_4 pos_6_4
0
4
0 0 0 8
0 3 0 1
0 4 1 0
0 6 1 0
1
end_operator
begin_operator
jump_continue_move pos_4_4 pos_5_4 pos_6_4
0
4
0 0 6 8
0 3 0 1
0 4 1 0
0 6 1 0
0
end_operator
begin_operator
end_move pos_0_2
0
1
0 0 16 0
0
end_operator
begin_operator
jump_new_move pos_3_2 pos_2_2 pos_1_2
0
4
0 0 0 12
0 13 1 0
0 15 1 0
0 16 1 0
1
end_operator
begin_operator
jump_new_move pos_3_2 pos_3_1 pos_3_0
0
4
0 0 0 15
0 8 0 1
0 13 1 0
0 18 0 1
1
end_operator
begin_operator
jump_continue_move pos_3_2 pos_2_2 pos_1_2
0
4
0 0 9 12
0 13 1 0
0 15 1 0
0 16 1 0
0
end_operator
begin_operator
jump_continue_move pos_3_2 pos_3_1 pos_3_0
0
4
0 0 9 15
0 8 0 1
0 13 1 0
0 18 0 1
0
end_operator
begin_operator
end_move pos_6_4
0
1
0 0 8 0
0
end_operator
begin_operator
jump_continue_move pos_0_2 pos_1_2 pos_2_2
0
4
0 0 16 3
0 1 0 1
0 15 0 1
0 16 0 1
0
end_operator
begin_operator
jump_new_move pos_3_1 pos_3_2 pos_3_3
0
4
0 0 0 7
0 2 0 1
0 8 0 1
0 13 1 0
1
end_operator
begin_operator
jump_new_move pos_2_2 pos_3_2 pos_4_2
0
4
0 0 0 19
0 13 1 0
0 15 1 0
0 19 1 0
1
end_operator
begin_operator
jump_new_move pos_0_2 pos_1_2 pos_2_2
0
4
0 0 0 3
0 1 0 1
0 15 0 1
0 16 0 1
1
end_operator
begin_operator
end_move pos_3_0
0
1
0 0 15 0
0
end_operator
begin_operator
jump_new_move pos_6_4 pos_5_4 pos_4_4
0
4
0 0 0 6
0 3 0 1
0 4 0 1
0 6 0 1
1
end_operator
begin_operator
jump_continue_move pos_6_4 pos_5_4 pos_4_4
0
4
0 0 8 6
0 3 0 1
0 4 0 1
0 6 0 1
0
end_operator
begin_operator
end_move pos_2_2
0
1
0 0 3 0
0
end_operator
begin_operator
end_move pos_3_3
0
1
0 0 7 0
0
end_operator
begin_operator
end_move pos_4_2
0
1
0 0 19 0
0
end_operator
begin_operator
jump_new_move pos_3_0 pos_3_1 pos_3_2
0
4
0 0 0 9
0 8 0 1
0 13 0 1
0 18 1 0
1
end_operator
begin_operator
jump_continue_move pos_3_0 pos_3_1 pos_3_2
0
4
0 0 15 9
0 8 0 1
0 13 0 1
0 18 1 0
0
end_operator
begin_operator
jump_continue_move pos_2_2 pos_1_2 pos_0_2
0
4
0 0 3 16
0 1 1 0
0 15 1 0
0 16 0 1
0
end_operator
begin_operator
jump_continue_move pos_2_2 pos_3_2 pos_4_2
0
4
0 0 3 19
0 13 1 0
0 15 1 0
0 19 1 0
0
end_operator
begin_operator
jump_new_move pos_3_3 pos_3_4 pos_3_5
0
4
0 0 0 10
0 2 1 0
0 17 1 0
0 20 0 1
1
end_operator
begin_operator
jump_continue_move pos_3_3 pos_3_4 pos_3_5
0
4
0 0 7 10
0 2 1 0
0 17 1 0
0 20 0 1
0
end_operator
begin_operator
jump_continue_move pos_3_3 pos_3_2 pos_3_1
0
4
0 0 7 4
0 2 1 0
0 8 1 0
0 13 1 0
0
end_operator
begin_operator
jump_new_move pos_4_2 pos_3_2 pos_2_2
0
4
0 0 0 3
0 13 1 0
0 15 0 1
0 19 0 1
1
end_operator
begin_operator
jump_continue_move pos_4_2 pos_3_2 pos_2_2
0
4
0 0 19 3
0 13 1 0
0 15 0 1
0 19 0 1
0
end_operator
begin_operator
jump_new_move pos_3_4 pos_3_3 pos_3_2
0
4
0 0 0 9
0 2 1 0
0 13 0 1
0 20 0 1
1
end_operator
begin_operator
jump_new_move pos_3_2 pos_3_3 pos_3_4
0
4
0 0 0 18
0 2 1 0
0 13 1 0
0 20 1 0
1
end_operator
begin_operator
jump_continue_move pos_3_2 pos_3_3 pos_3_4
0
4
0 0 9 18
0 2 1 0
0 13 1 0
0 20 1 0
0
end_operator
begin_operator
jump_continue_move pos_3_4 pos_3_3 pos_3_2
0
4
0 0 18 9
0 2 1 0
0 13 0 1
0 20 0 1
0
end_operator
begin_operator
jump_new_move pos_3_2 pos_4_2 pos_5_2
0
4
0 0 0 13
0 5 0 1
0 13 1 0
0 19 0 1
1
end_operator
begin_operator
jump_continue_move pos_3_2 pos_4_2 pos_5_2
0
4
0 0 9 13
0 5 0 1
0 13 1 0
0 19 0 1
0
end_operator
begin_operator
jump_new_move pos_3_3 pos_3_2 pos_3_1
0
4
0 0 0 4
0 2 1 0
0 8 1 0
0 13 1 0
1
end_operator
begin_operator
end_move pos_3_5
0
1
0 0 10 0
0
end_operator
begin_operator
end_move pos_3_1
0
1
0 0 4 0
0
end_operator
begin_operator
end_move pos_5_2
0
1
0 0 13 0
0
end_operator
begin_operator
jump_new_move pos_3_5 pos_3_4 pos_3_3
0
4
0 0 0 7
0 2 0 1
0 17 0 1
0 20 0 1
1
end_operator
begin_operator
jump_continue_move pos_3_5 pos_3_4 pos_3_3
0
4
0 0 10 7
0 2 0 1
0 17 0 1
0 20 0 1
0
end_operator
begin_operator
jump_continue_move pos_3_1 pos_3_2 pos_3_3
0
4
0 0 4 7
0 2 0 1
0 8 0 1
0 13 1 0
0
end_operator
begin_operator
jump_new_move pos_3_4 pos_3_5 pos_3_6
0
4
0 0 0 11
0 14 1 0
0 17 0 1
0 20 0 1
1
end_operator
begin_operator
jump_continue_move pos_3_4 pos_3_5 pos_3_6
0
4
0 0 18 11
0 14 1 0
0 17 0 1
0 20 0 1
0
end_operator
begin_operator
jump_new_move pos_5_2 pos_4_2 pos_3_2
0
4
0 0 0 9
0 5 1 0
0 13 0 1
0 19 0 1
1
end_operator
begin_operator
jump_continue_move pos_5_2 pos_4_2 pos_3_2
0
4
0 0 13 9
0 5 1 0
0 13 0 1
0 19 0 1
0
end_operator
begin_operator
jump_new_move pos_4_2 pos_5_2 pos_6_2
0
4
0 0 0 14
0 5 1 0
0 10 0 1
0 19 0 1
1
end_operator
begin_operator
jump_continue_move pos_4_2 pos_5_2 pos_6_2
0
4
0 0 19 14
0 5 1 0
0 10 0 1
0 19 0 1
0
end_operator
begin_operator
end_move pos_3_6
0
1
0 0 11 0
0
end_operator
begin_operator
end_move pos_6_2
0
1
0 0 14 0
0
end_operator
begin_operator
jump_new_move pos_3_6 pos_3_5 pos_3_4
0
4
0 0 0 18
0 14 0 1
0 17 0 1
0 20 1 0
1
end_operator
begin_operator
jump_continue_move pos_3_6 pos_3_5 pos_3_4
0
4
0 0 11 18
0 14 0 1
0 17 0 1
0 20 1 0
0
end_operator
begin_operator
jump_new_move pos_6_2 pos_5_2 pos_4_2
0
4
0 0 0 19
0 5 1 0
0 10 1 0
0 19 1 0
1
end_operator
begin_operator
jump_continue_move pos_6_2 pos_5_2 pos_4_2
0
4
0 0 14 19
0 5 1 0
0 10 1 0
0 19 1 0
0
end_operator
0
