echo "running integration with mc rejection sampling"
python3 $PWD/python/myrandom.py -Nsample 100
echo "running integration with trapezoidal methode"
python3 $PWD/python/integrator.py -step 100 --trapezoidal -limit 0 3
