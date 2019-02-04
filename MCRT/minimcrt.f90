module rand
    implicit none
    
    contains
    
    real function ran2()

        implicit none

        call random_number(ran2)

    end function ran2


    subroutine scatter(dir, pi)

        implicit none
        
        real, intent(INOUT) :: dir(:)
        real, intent(IN)    :: pi
        
        real :: cost, sint, phi

        cost = 2.*ran2() - 1.
        sint = sqrt(1. - cost*cost)
        phi = 2.*pi*ran2()
        dir = [sint*cos(phi), sint*sin(phi), cost]


    end subroutine scatter

end module rand

program simpleMCRT

    use rand

    implicit none
    
    real    :: pos(3), dir(3), phi, tau, pi, sint, cost, L, taumax, R, albedo
    integer :: i, nphot, nscat

    albedo = 1.
    pi = 4.*atan(1.)
    nphot = 100000
    taumax = 10.
    R = 1.
    nscat = 0
    do i = 1, Nphot

        pos = 0.

        tau = -log(ran2())
        call scatter(dir, pi)
        do 
            L = (tau / taumax) * R
            pos = pos + dir * L
            if(ran2() < albedo)then
                nscat = nscat + 1
                call scatter(dir, pi)
                tau = -log(ran2())
            else
                exit
            end if
            if(dot_product(pos, pos) > R)exit
        end do

    end do
    print*,real(nscat)/real(nphot)
end program simpleMCRT