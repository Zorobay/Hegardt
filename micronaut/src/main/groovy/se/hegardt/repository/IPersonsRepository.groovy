package se.hegardt.repository

import io.micronaut.data.annotation.Query
import io.micronaut.data.annotation.Repository
import io.micronaut.data.jpa.repository.JpaRepository
import se.hegardt.domain.Person

@Repository
interface IPersonsRepository extends JpaRepository<Person, Long> {

    @Query('SELECT p FROM Person p WHERE p.father.id = :personId OR p.mother.id = :personId')
    List<Person> findChildren(Long personId)

    @Query('''
        SELECT p FROM Person p
        WHERE p.normalizedName LIKE CONCAT('%', :token, '%')
    ''')
    List<Person> findByNameToken(String token)
}
