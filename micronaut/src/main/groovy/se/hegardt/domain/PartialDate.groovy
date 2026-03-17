package se.hegardt.domain

import groovy.transform.CompileStatic
import jakarta.annotation.Nullable
import jakarta.persistence.Embeddable
import jakarta.persistence.PrePersist
import jakarta.persistence.PreUpdate

import java.time.LocalDate

@Embeddable
@CompileStatic
class PartialDate {

    @Nullable
    LocalDate date

    @Nullable
    Integer year

    @Nullable
    Integer month

    @Nullable
    Integer day

    @PrePersist
    @PreUpdate
    void computeDate() {
        if (!year) {
            date = null
            return
        }
        date = LocalDate.of(year, month ?: 1, day ?: 1)
    }
}
