package se.hegardt.repository

import io.micronaut.data.annotation.Query
import io.micronaut.data.annotation.Repository
import io.micronaut.data.jpa.repository.JpaRepository
import se.hegardt.domain.Person

@Repository
interface PersonsRepository extends JpaRepository<Person, Long> {

    @Query("SELECT p FROM Person p WHERE p.father.id = :personId OR p.mother.id = :personId")
    List<Person> findChildren(Long personId)

    List<Person> findByLastName(String lastName)

    List<Person> findByFirstNameAndLastName(String firstName, String lastName)
}
