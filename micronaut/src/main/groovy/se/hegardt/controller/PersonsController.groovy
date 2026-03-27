package se.hegardt.controller

import groovy.transform.CompileStatic
import io.micronaut.http.HttpResponse
import io.micronaut.http.annotation.Controller
import io.micronaut.http.annotation.Get
import se.hegardt.domain.Person
import se.hegardt.dto.PersonDto
import se.hegardt.dto.PersonDto
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

    @Get('/getAllMap')
    HttpResponse<Map<Long, PersonDto>> getAllMap() {
        return HttpResponse.ok(personsService.findAll().collectEntries { Person p -> [(p.id): PersonDto.from(p)] })
    }

    @Get('/findByName/{name}')
    HttpResponse<List<PersonDto>> findByName(String name) {
        return HttpResponse.ok(personsService.findByName(name).collect { Person p -> PersonDto.from(p) })
    }

    @Get('/getById/{id}')
    HttpResponse<PersonDto> getById(int id) {
        return personsService.getById(id)
            .map { Person p -> HttpResponse.ok(PersonDto.from(p)) }
            .orElse(HttpResponse.notFound())
    }

    @Get('/getCompleteById/{id}')
    HttpResponse<PersonDto> getCompleteById(int id) {
        return personsService.getCompleteById(id)
            .map { PersonDto p -> HttpResponse.ok(p) }
            .orElse(HttpResponse.notFound())
    }

}
