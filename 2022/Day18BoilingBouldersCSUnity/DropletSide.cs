using UnityEngine;

// Is placed to cubes box collider sides that when they touch eachother 
// they both destroy themselves making it possible to solve p1 by counting
// remaining box colliders
public class DropletSide : MonoBehaviour
{
    void OnCollisionEnter(Collision collision)
    {
        Destroy(gameObject);
    }
}
