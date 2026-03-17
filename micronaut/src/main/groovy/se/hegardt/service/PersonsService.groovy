package se.hegardt.service

import groovy.transform.CompileStatic
import jakarta.inject.Singleton
import se.hegardt.domain.Person
import se.hegardt.repository.PersonsRepository

@Singleton
@CompileStatic
class PersonsService {
    private final PersonsRepository repository

    PersonsService(PersonsRepository repository) {
        this.repository = repository
    }

    List<Person> findAll() {
        return repository.findAll().toList()
    }

    Optional<Person> findById(Long id) {
        return repository.findById(id)
    }

//    Optional<Person> findByFileId(Integer fileId) {
//        return repository.findByFileId(fileId)
//    }

    List<Person> findByLastName(String lastName) {
        return repository.findByLastName(lastName)
    }

    List<Person> findByFirstNameAndLastName(String firstName, String lastName) {
        return repository.findByFirstNameAndLastName(firstName, lastName)
    }

    Person save(Person person) {
        return repository.save(person)
    }

    Person merge(Person person) {
        return repository.merge(person)
    }

    Person update(Person person) {
        return repository.update(person)
    }

    void delete(Long id) {
        repository.deleteById(id)
    }
}
