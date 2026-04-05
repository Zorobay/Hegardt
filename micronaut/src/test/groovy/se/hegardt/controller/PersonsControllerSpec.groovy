package se.hegardt.controller

import io.micronaut.http.HttpResponse
import io.micronaut.http.HttpStatus
import se.hegardt.dto.PersonSummaryDto
import se.hegardt.dto.tree.PersonTreeRootDto
import se.hegardt.service.IPersonsService
import spock.lang.Specification

class PersonsControllerSpec extends Specification {

    IPersonsService personsService = Mock()
    PersonsController controller = new PersonsController(personsService)

    def 'getTreeRootById: returns ok when person found'() {
        given:
            PersonTreeRootDto dto = new PersonTreeRootDto(
                firstName: 'Seb',
                children: [new PersonSummaryDto(firstName: 'Lena')]
            )
            personsService.getTreeRootById(1L) >> Optional.of(dto)

        when:
            HttpResponse<PersonTreeRootDto> response = controller.getTreeRootById(1L)

        then:
            response.status == HttpStatus.OK
            response.body() == dto
    }

    def 'getTreeRootById: returns not found when person absent'() {
        given:
            personsService.getTreeRootById(99L) >> Optional.empty()

        when:
            HttpResponse<PersonTreeRootDto> response = controller.getTreeRootById(99L)

        then:
            response.status == HttpStatus.NOT_FOUND
    }
}
