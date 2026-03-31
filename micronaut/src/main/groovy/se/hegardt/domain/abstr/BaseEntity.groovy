package se.hegardt.domain.abstr

import groovy.transform.CompileStatic
import groovy.transform.EqualsAndHashCode
import jakarta.persistence.Column
import jakarta.persistence.Id
import jakarta.persistence.MappedSuperclass
import jakarta.persistence.PrePersist
import jakarta.persistence.PreUpdate
import jakarta.persistence.Version

import java.time.Instant

@MappedSuperclass
@EqualsAndHashCode(includes = ['id'])
@CompileStatic
@SuppressWarnings(['AbstractClassWithoutAbstractMethod'])
abstract class BaseEntity {

    @Id
    Long id

    @Version
    Long version = 0L

    @Column(updatable = false)
    Instant createdAt

    Instant updatedAt

    @PrePersist
    void onCreate() {
        createdAt = Instant.now()
        updatedAt = Instant.now()
    }

    @PreUpdate
    void onUpdate() {
        updatedAt = Instant.now()
    }
}
