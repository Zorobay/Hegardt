package se.hegardt.controller

import groovy.transform.CompileStatic
import io.micronaut.http.HttpResponse
import io.micronaut.http.annotation.Controller
import io.micronaut.http.annotation.Get
import se.hegardt.domain.Person
import se.hegardt.dto.PersonSummaryDto
import se.hegardt.service.PersonsService

@Controller('/persons')
@CompileStatic
class PersonsController {

    private final PersonsService personsService

    PersonsController(PersonsService personsService) {
        this.personsService = personsService
    }

    @Get('/getAll')
    HttpResponse<List<PersonSummaryDto>> getAll() {
        return HttpResponse.ok(personsService.findAll().collect { Person p -> PersonSummaryDto.from(p) })
    }

    @Get('/getPersonById/{id}')
    HttpResponse<Person> getPersonById(int id) {
        return personsService.findById(id)
            .map { Person p -> HttpResponse.ok(p) }
            .orElse(HttpResponse.notFound())
    }

}
