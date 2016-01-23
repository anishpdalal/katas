(ns langton.ant-test
  (:use midje.sweet)
  (:use [langton.ant]))

(def ant (create))

(facts "about creating ants"
  (fact "a new ant starts at the origin"
    (:pos ant) => [0 0])

  (fact "a new ant starts facing north"
     (:faces ant) => :north))

(facts "about turning"
  (fact "it turns left when given :black"
    (map :faces (take 5 (iterate #(turn % :black) ant)))
      => [:north :west :south :east :north])

  (fact "it turns right when given :white"
    (map :faces (take 5 (iterate #(turn % :white) ant)))
      => [:north :east :south :west :north]))

(facts "about stepping"
  (fact "it advances forward by one"
    (:pos (step (create :pos [0 0] :faces :north))) => [ 0  1]
    (:pos (step (create :pos [0 0] :faces :west ))) => [-1  0]
    (:pos (step (create :pos [0 0] :faces :south))) => [ 0 -1]
    (:pos (step (create :pos [0 0] :faces :east ))) => [ 1  0]))
