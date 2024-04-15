(define (problem robot-world-problem)
  (:domain robot-world)

  ;; Objetos
  (:objects 
    robot1 - robot
    person1 - person
    room1 room2 - room
    accelerometer heart-monitor camera - device
  )

  ;; Estado inicial
  (:init
    (at robot1 room1)
    (in person1 room1)
    (active accelerometer)
    (not (person-state-known person1)) ; El estado de la persona es desconocido al principio
    ;;; Otros predicados iniciales si los hay
  )

  ;; Objetivo
  (:goal 
    (person-state-known person1) ; El objetivo es conocer el estado de la persona
  )
)