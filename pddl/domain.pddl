(define (domain robot-world)
  (:requirements :typing)

  ;; Definicion de tipos
  (:types room robot person device)

  ;; Definicion de predicados
  (:predicates
    (at ?r - robot ?l - room)
    (in ?p - person ?l - room)
    (active ?d - device)
    (detected-fall)
    (detected-heart-attack)
    (camera-checked)
    (person-state-known ?p - person)
  )

  ;; Acciones
  (:action move
    :parameters (?r - robot ?from - room ?to - room)
    :precondition (and (at ?r ?from))
    :effect (and (not (at ?r ?from)) (at ?r ?to))
  )

  (:action ask-if-ok
    :parameters (?r - robot ?p - person ?l - room)
    :precondition (and (at ?r ?l) (in ?p ?l))
    :effect (and (person-state-known ?p) (detected-heart-attack))
  )

  (:action check-camera
    :parameters (?r - robot ?p - person ?l - room)
    :precondition (and (at ?r ?l) (in ?p ?l) (active ?camera))
    :effect (and (person-state-known ?p) (detected-fall) (camera-checked))
  )

    (:action check-for-heart-attack
    :parameters (?r - robot ?p - person)
    :precondition (in ?p ?l)
    :effect (checked-for-heart-attack)
  )
)