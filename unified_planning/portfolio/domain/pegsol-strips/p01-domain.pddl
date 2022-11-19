;; Peg Solitaire sequential domain

(define (domain pegsolitaire-sequential)
    (:requirements :typing :action-costs)
    (:types location - object)
    (:predicates
        (IN_LINE ?x ?y ?z - location)
        (occupied ?l - location)
        (free ?l - location)
        (move_ended)
        (last_visited ?l - location)
    )
    (:functions (total-cost) - number)

    (:action jump_new_move
     :parameters (?from - location ?over - location ?to - location)
     :precondition (and 
                       (move_ended)
                       (IN_LINE ?from ?over ?to)
                       (occupied ?from)
                       (occupied ?over)
                       (free ?to)
                   )
     :effect (and
                 (not (move_ended))
                 (not (occupied ?from))
                 (not (occupied ?over))
                 (not (free ?to))
                 (free ?from)
                 (free ?over)
                 (occupied ?to)
                 (last_visited ?to)
                 (increase (total-cost) 1)
             )
    )

    (:action jump_continue_move
     :parameters (?from - location ?over - location ?to - location)
     :precondition (and 
                       (last_visited ?from)
                       (IN_LINE ?from ?over ?to)
                       (occupied ?from)
                       (occupied ?over)
                       (free ?to)
                   )
     :effect (and
                 (not (occupied ?from))
                 (not (occupied ?over))
                 (not (free ?to))
                 (free ?from)
                 (free ?over)
                 (occupied ?to)
                 (not (last_visited ?from))
                 (last_visited ?to)
             )
    )

    (:action end_move
     :parameters (?loc - location)
     :precondition (last_visited ?loc)
     :effect (and
                 (move_ended)
                 (not (last_visited ?loc))
             )
    )
)
