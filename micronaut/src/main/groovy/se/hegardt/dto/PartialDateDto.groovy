package se.hegardt.dto

import groovy.transform.CompileStatic
import io.micronaut.serde.annotation.Serdeable
import se.hegardt.domain.PartialDate

import java.time.LocalDate

@Serdeable
@CompileStatic
class PartialDateDto {
    Integer day
    Integer month
    Integer year
    LocalDate date

    static PartialDateDto from(PartialDate date) {
        if (!date) return new PartialDateDto()
        return new PartialDateDto(
            day: date.day,
            month: date.month,
            year: date.year,
            date: date.date
        )
    }
}
