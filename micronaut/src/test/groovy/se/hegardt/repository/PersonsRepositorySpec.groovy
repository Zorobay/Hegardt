package se.hegardt.repository

import io.micronaut.test.extensions.spock.annotation.MicronautTest
import jakarta.inject.Inject
import se.hegardt.domain.Person
import spock.lang.Specification

@MicronautTest
class PersonsRepositorySpec extends Specification {
    @Inject
    PersonsRepository personsRepository

    void setup() {
        personsRepository.save(new Person(id: 1, firstName: 'Johan', lastName: 'Hegardt'))
        personsRepository.save(new Person(id: 2, firstName: 'Sebastian', middleNames: 'Lechard', lastName: 'Hegardt',))
        personsRepository.save(new Person(id: 3, firstName: 'Sebastian', lastName: 'Svensson'))
        personsRepository.save(new Person(id: 4, firstName: 'Anna', lastName: 'Hegardt'))
        personsRepository.save(new Person(id: 5, firstName: 'Erik', lastName: 'Svensson'))
        personsRepository.save(new Person(id: 6, firstName: "Ásh'Niûpurh", lastName: 'Żółćiński-Håvårdsvær'))
    }

    void cleanup() {
        personsRepository.deleteAll()
    }

    def "findByNameTokens"() {
        when:
            List<Person> res = personsRepository.findByNameTokens(tokens)
        then:
            res.collect { it.id }.toSet() == (expectedIds.toSet() as Set<Long>)
        where:
            tokens                   | expectedIds
            ['sebastian']            | [2, 3]
            ['sebastian', 'hegardt'] | [2]
            ['hegardt']              | [1, 2, 4]
            ['t', 'a', 'n']          | [1, 2, 3, 4]
            ['k', 'v', 'p']          | [6]
            ['seb', 'ö']             | []
            ['a']                    | [1, 2, 3, 4, 6]
    }

}
