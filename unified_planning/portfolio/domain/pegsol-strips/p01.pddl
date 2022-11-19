;; The following problem is taken from the problem library of Solipeg 2.2:
;; 
;; Solipeg, a Classic Marble Puzzle Game for the
;; Psion Series 3a, 3c and Siena
;; Version 2.2 (and 2.2 Lite)
;; Copyright (C) 1993, 1994, 1995, 1996 J Cade Roux
;; 
;; This program is free software; you can redistribute it and/or modify
;; it under the terms of the GNU General Public License as published by
;; the Free Software Foundation; either version 2 of the License, or
;; (at your option) any later version.
;; 
;; This program is distributed in the hope that it will be useful,
;; but WITHOUT ANY WARRANTY; without even the implied warranty of
;; MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
;; GNU General Public License for more details.
;; 
;; You should have received a copy of the GNU General Public License
;; along with this program; if not, write to the Free Software
;; Foundation, Inc., 675 Mass Ave, Cambridge, MA 02139, USA.
;; 
;; (see http://ourworld.compuserve.com/homepages/cade/psionsof.htm,
;; http://ourworld.compuserve.com/homepages/cade/solsrc22.zip)
;; 
;; The Solipeg problem library in turn is derived from the booklet
;; "Problems in Puzzle-Peg" included in the game Puzzle-Peg (Third
;; Edition, 1924, Lubbers & Bell Mfg. Co.,Clinton, Iowa, USA).
;; 
;; Original problem number and name: "2 Novice"
;; 
;; Number of pegs:                  5
;; Number of diagonal moves needed: 0
;; 
;; Problem description:
;; "*" denotes "occupied"
;; "o" denotes "free"
;; 
;;     o o o     
;;     o * o     
;; o o * o * o o 
;; o * o o * o o 
;; o o o o o o o 
;;     o o o     
;;     o o o     
;; 
;; Target position = (3,3)
;; 
(define (problem pegsolitaire-sequential-002)
    (:domain pegsolitaire-sequential)
    (:objects
        pos_0_2 - location
        pos_0_3 - location
        pos_0_4 - location
        pos_1_2 - location
        pos_1_3 - location
        pos_1_4 - location
        pos_2_0 - location
        pos_2_1 - location
        pos_2_2 - location
        pos_2_3 - location
        pos_2_4 - location
        pos_2_5 - location
        pos_2_6 - location
        pos_3_0 - location
        pos_3_1 - location
        pos_3_2 - location
        pos_3_3 - location
        pos_3_4 - location
        pos_3_5 - location
        pos_3_6 - location
        pos_4_0 - location
        pos_4_1 - location
        pos_4_2 - location
        pos_4_3 - location
        pos_4_4 - location
        pos_4_5 - location
        pos_4_6 - location
        pos_5_2 - location
        pos_5_3 - location
        pos_5_4 - location
        pos_6_2 - location
        pos_6_3 - location
        pos_6_4 - location
    )
    (:init
        (= (total-cost) 0)
        (move_ended)
        (IN_LINE pos_0_2 pos_0_3 pos_0_4)
        (IN_LINE pos_0_4 pos_0_3 pos_0_2)
        (IN_LINE pos_0_2 pos_1_2 pos_2_2)
        (IN_LINE pos_2_2 pos_1_2 pos_0_2)
        (IN_LINE pos_0_3 pos_1_3 pos_2_3)
        (IN_LINE pos_2_3 pos_1_3 pos_0_3)
        (IN_LINE pos_0_4 pos_1_4 pos_2_4)
        (IN_LINE pos_2_4 pos_1_4 pos_0_4)
        (IN_LINE pos_1_2 pos_1_3 pos_1_4)
        (IN_LINE pos_1_4 pos_1_3 pos_1_2)
        (IN_LINE pos_1_2 pos_2_2 pos_3_2)
        (IN_LINE pos_3_2 pos_2_2 pos_1_2)
        (IN_LINE pos_1_3 pos_2_3 pos_3_3)
        (IN_LINE pos_3_3 pos_2_3 pos_1_3)
        (IN_LINE pos_1_4 pos_2_4 pos_3_4)
        (IN_LINE pos_3_4 pos_2_4 pos_1_4)
        (IN_LINE pos_2_0 pos_2_1 pos_2_2)
        (IN_LINE pos_2_2 pos_2_1 pos_2_0)
        (IN_LINE pos_2_0 pos_3_0 pos_4_0)
        (IN_LINE pos_4_0 pos_3_0 pos_2_0)
        (IN_LINE pos_2_1 pos_2_2 pos_2_3)
        (IN_LINE pos_2_3 pos_2_2 pos_2_1)
        (IN_LINE pos_2_1 pos_3_1 pos_4_1)
        (IN_LINE pos_4_1 pos_3_1 pos_2_1)
        (IN_LINE pos_2_2 pos_2_3 pos_2_4)
        (IN_LINE pos_2_4 pos_2_3 pos_2_2)
        (IN_LINE pos_2_2 pos_3_2 pos_4_2)
        (IN_LINE pos_4_2 pos_3_2 pos_2_2)
        (IN_LINE pos_2_3 pos_2_4 pos_2_5)
        (IN_LINE pos_2_5 pos_2_4 pos_2_3)
        (IN_LINE pos_2_3 pos_3_3 pos_4_3)
        (IN_LINE pos_4_3 pos_3_3 pos_2_3)
        (IN_LINE pos_2_4 pos_2_5 pos_2_6)
        (IN_LINE pos_2_6 pos_2_5 pos_2_4)
        (IN_LINE pos_2_4 pos_3_4 pos_4_4)
        (IN_LINE pos_4_4 pos_3_4 pos_2_4)
        (IN_LINE pos_2_5 pos_3_5 pos_4_5)
        (IN_LINE pos_4_5 pos_3_5 pos_2_5)
        (IN_LINE pos_2_6 pos_3_6 pos_4_6)
        (IN_LINE pos_4_6 pos_3_6 pos_2_6)
        (IN_LINE pos_3_0 pos_3_1 pos_3_2)
        (IN_LINE pos_3_2 pos_3_1 pos_3_0)
        (IN_LINE pos_3_1 pos_3_2 pos_3_3)
        (IN_LINE pos_3_3 pos_3_2 pos_3_1)
        (IN_LINE pos_3_2 pos_3_3 pos_3_4)
        (IN_LINE pos_3_4 pos_3_3 pos_3_2)
        (IN_LINE pos_3_2 pos_4_2 pos_5_2)
        (IN_LINE pos_5_2 pos_4_2 pos_3_2)
        (IN_LINE pos_3_3 pos_3_4 pos_3_5)
        (IN_LINE pos_3_5 pos_3_4 pos_3_3)
        (IN_LINE pos_3_3 pos_4_3 pos_5_3)
        (IN_LINE pos_5_3 pos_4_3 pos_3_3)
        (IN_LINE pos_3_4 pos_3_5 pos_3_6)
        (IN_LINE pos_3_6 pos_3_5 pos_3_4)
        (IN_LINE pos_3_4 pos_4_4 pos_5_4)
        (IN_LINE pos_5_4 pos_4_4 pos_3_4)
        (IN_LINE pos_4_0 pos_4_1 pos_4_2)
        (IN_LINE pos_4_2 pos_4_1 pos_4_0)
        (IN_LINE pos_4_1 pos_4_2 pos_4_3)
        (IN_LINE pos_4_3 pos_4_2 pos_4_1)
        (IN_LINE pos_4_2 pos_4_3 pos_4_4)
        (IN_LINE pos_4_4 pos_4_3 pos_4_2)
        (IN_LINE pos_4_2 pos_5_2 pos_6_2)
        (IN_LINE pos_6_2 pos_5_2 pos_4_2)
        (IN_LINE pos_4_3 pos_4_4 pos_4_5)
        (IN_LINE pos_4_5 pos_4_4 pos_4_3)
        (IN_LINE pos_4_3 pos_5_3 pos_6_3)
        (IN_LINE pos_6_3 pos_5_3 pos_4_3)
        (IN_LINE pos_4_4 pos_4_5 pos_4_6)
        (IN_LINE pos_4_6 pos_4_5 pos_4_4)
        (IN_LINE pos_4_4 pos_5_4 pos_6_4)
        (IN_LINE pos_6_4 pos_5_4 pos_4_4)
        (IN_LINE pos_5_2 pos_5_3 pos_5_4)
        (IN_LINE pos_5_4 pos_5_3 pos_5_2)
        (IN_LINE pos_6_2 pos_6_3 pos_6_4)
        (IN_LINE pos_6_4 pos_6_3 pos_6_2)
        (free pos_0_2)
        (free pos_0_3)
        (free pos_0_4)
        (free pos_1_2)
        (free pos_1_4)
        (free pos_2_0)
        (free pos_2_1)
        (free pos_2_3)
        (free pos_2_5)
        (free pos_2_6)
        (free pos_3_0)
        (free pos_3_2)
        (free pos_3_3)
        (free pos_3_5)
        (free pos_3_6)
        (free pos_4_0)
        (free pos_4_1)
        (free pos_4_2)
        (free pos_4_3)
        (free pos_4_4)
        (free pos_4_5)
        (free pos_4_6)
        (free pos_5_2)
        (free pos_5_3)
        (free pos_5_4)
        (free pos_6_2)
        (free pos_6_3)
        (free pos_6_4)
        (occupied pos_1_3)
        (occupied pos_2_2)
        (occupied pos_2_4)
        (occupied pos_3_1)
        (occupied pos_3_4)
    )
    (:goal (and
        (free pos_0_2)
        (free pos_0_3)
        (free pos_0_4)
        (free pos_1_2)
        (free pos_1_3)
        (free pos_1_4)
        (free pos_2_0)
        (free pos_2_1)
        (free pos_2_2)
        (free pos_2_3)
        (free pos_2_4)
        (free pos_2_5)
        (free pos_2_6)
        (free pos_3_0)
        (free pos_3_1)
        (free pos_3_2)
        (free pos_3_4)
        (free pos_3_5)
        (free pos_3_6)
        (free pos_4_0)
        (free pos_4_1)
        (free pos_4_2)
        (free pos_4_3)
        (free pos_4_4)
        (free pos_4_5)
        (free pos_4_6)
        (free pos_5_2)
        (free pos_5_3)
        (free pos_5_4)
        (free pos_6_2)
        (free pos_6_3)
        (free pos_6_4)
        (occupied pos_3_3)
           )
    )
    (:metric minimize (total-cost))
)
