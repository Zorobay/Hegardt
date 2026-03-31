//file:noinspection ChangeToOperator
package se.hegardt.repository

import groovy.transform.CompileStatic
import io.micronaut.data.annotation.Query
import io.micronaut.data.annotation.Repository
import io.micronaut.data.jpa.repository.JpaRepository
import io.micronaut.transaction.annotation.Transactional
import jakarta.persistence.EntityManager
import jakarta.persistence.criteria.CriteriaBuilder
import jakarta.persistence.criteria.CriteriaQuery
import jakarta.persistence.criteria.Predicate
import jakarta.persistence.criteria.Root
import se.hegardt.domain.Person

@Repository
@CompileStatic
abstract class PersonsRepository implements JpaRepository<Person, Long> {

    private final EntityManager entityManager

    PersonsRepository(EntityManager entityManager) {
        this.entityManager = entityManager
    }

    @Query('SELECT p FROM Person p WHERE p.father.id = :personId OR p.mother.id = :personId')
    abstract List<Person> findChildren(Long personId)

    @Transactional
    List<Person> findByNameTokens(List<String> tokens) {
        CriteriaBuilder cb = entityManager.criteriaBuilder
        CriteriaQuery<Person> q = cb.createQuery(Person)
        Root<Person> root = q.from(Person)

        List<Predicate> predicates = tokens.collect { String token ->
            cb.like(root.get('normalizedName'), "%${token}%")
        }

        q.where(cb.and(predicates as Predicate[]))
        return entityManager.createQuery(q).resultList
    }
}
