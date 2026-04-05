package se.hegardt.controller

import groovy.transform.CompileStatic
import io.micronaut.http.HttpResponse
import io.micronaut.http.annotation.Controller
import io.micronaut.http.annotation.Get
import se.hegardt.domain.Person
import se.hegardt.dto.PersonDto
import se.hegardt.dto.PersonSummaryDto
import se.hegardt.dto.tree.PersonTreeRootDto
import se.hegardt.service.IPersonsService

@Controller('/persons')
@CompileStatic
class PersonsController {

    private final IPersonsService personsService

    PersonsController(IPersonsService personsService) {
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
    HttpResponse<List<PersonSummaryDto>> findByName(String name) {
        return HttpResponse.ok(personsService.findByName(name).collect { Person p -> PersonSummaryDto.from(p) })
    }

    @Get('/getSummaryById/{id}')
    HttpResponse<PersonSummaryDto> getSummaryById(long id) {
        return personsService.getById(id)
            .map { Person p -> HttpResponse.ok(PersonSummaryDto.from(p)) }
            .orElse(HttpResponse.notFound())
    }

    @Get('/getCompleteById/{id}')
    HttpResponse<PersonDto> getCompleteById(long id) {
        return personsService.getCompleteById(id)
            .map { PersonDto p -> HttpResponse.ok(p) }
            .orElse(HttpResponse.notFound())
    }

    @Get('/getTreeRootById/{id}')
    HttpResponse<PersonTreeRootDto> getTreeRootById(long id) {
        return personsService.getTreeRootById(id)
            .map { PersonTreeRootDto root -> HttpResponse.ok(root) }
            .orElse(HttpResponse.notFound())
    }

}
