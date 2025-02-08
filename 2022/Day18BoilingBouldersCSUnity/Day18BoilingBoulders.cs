using System.Collections.Generic;
using UnityEngine;
using Sirenix.OdinInspector;

public class Day18BoilingBoulders : MonoBehaviour
{
    [SerializeField] private TextAsset _dropletsText;
    [SerializeField] private GameObject _droplet;
    private GameObject _dropletParent;

    void Awake()
    {
        _dropletParent = new GameObject("droplet parent");
    }

    [Button]
    void SpawnLavaDroplets()
    {
        int x = 0, y = 1, z = 2;

        var s = _dropletsText.text;  
        var droplets = new List<string>(s.Split('\n'));
        foreach (var item in droplets)
        {
            var coordinates = item.Split(',');
            Instantiate(
                _droplet, 
                new Vector3(float.Parse(coordinates[x]), 
                            float.Parse(coordinates[y]), 
                            float.Parse(coordinates[z])), 
                Quaternion.identity, 
                _dropletParent.transform);
        }

        Destroy(_droplet);
    }

    [Button]
    void BoxColliderAmount()
    {
        print(GameObject.FindObjectsOfType<BoxCollider>().Length);
    }
}
