def test_all():
    try:
        # Test entities interoperability
        interval = Interval()
        d0 = Direction(0)
        d1 = Direction(1)
        d2 = Direction(2)

        f00 = Face(d0, 0)
        f01 = Face(d0, 1)
        f10 = Face(d1, 0)
        f11 = Face(d1, 1)
        f20 = Face(d2, 0)
        f21 = Face(d2, 1)

        assert f20.opposite() == f21, "Opposite of (d2,0) should be (d2,1)"
        assert f10.opposite() == f11, "Opposite of (d1,1) should be (d1,0)"

        # Test const paths
        p_const = interval.path(1,1)
        assert  p_const(9) == 1, "Const path have to return const val"
        p_const_1 = interval.degeneracy(1)
        assert  p_const(9) == 1, "Const path have to return const val"


        # Test corresponsence between directions and faces
        assert f00.direction == d0, "Incorrect correspondence between face and direction" 
        assert f01.direction == d0, "Incorrect correspondence between face and direction" 

        assert f10.direction == d1, "Incorrect correspondence between face and direction" 
        assert f11.direction == d1, "Incorrect correspondence between face and direction" 

        assert f20.direction == d2, "Incorrect correspondence between face and direction" 
        assert f21.direction == d2, "Incorrect correspondence between face and direction" 


        # Test values consitency
        path = interval.path(0,1)
        assert path(f01.value) == path(f00.opposite().value)
        assert path(f00.value) == path(f01.opposite().value)


        print("All complex tests passed successfully!")
        return True

    except Exception as e:
        print(f"Face test failed: {str(e)}")

        return False
