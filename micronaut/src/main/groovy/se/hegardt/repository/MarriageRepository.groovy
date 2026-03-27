package se.hegardt.repository

import io.micronaut.data.annotation.Query
import io.micronaut.data.annotation.Repository
import io.micronaut.data.jpa.repository.JpaRepository
import se.hegardt.domain.Marriage

@Repository
interface MarriageRepository extends JpaRepository<Marriage, Long> {

    @Query("""
    SELECT DISTINCT m FROM Marriage m
    LEFT JOIN FETCH m.spouse1
    LEFT JOIN FETCH m.spouse2
    WHERE m.spouse1.id = :personId OR m.spouse2.id = :personId
""")
    List<Marriage> findAllByPersonId(Long personId)
}
