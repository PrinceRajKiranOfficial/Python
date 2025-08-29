# Object-Oriented Programming Concepts: Encapsulation vs Abstraction

## 📌 Encapsulation
- **Definition:** Encapsulation is the process of bundling data (variables) and methods (functions) that operate on that data into a single unit called a *class*.  
- **Purpose:** It hides the **internal data** of an object from the outside world and only exposes what is necessary.  
- **Key Point:** Access to the data is controlled through access modifiers (`private`, `protected`, `public`).  

### ✅ Example
```java
class Student {
    private String name;  // hidden data (encapsulation)

    // Public getter and setter methods to access private data
    public void setName(String name) {
        this.name = name;
    }
    public String getName() {
        return name;
    }
}
```

---

## 📌 Abstraction
- **Definition:** Abstraction is the process of hiding the **implementation details** and showing only the **functionality** to the user.  
- **Purpose:** It hides the internal **functionalities** of how things work, and only exposes *what* operations are available, not *how* they are performed.  
- **Key Point:** Achieved using **abstract classes** and **interfaces** in most OOP languages.  

### ✅ Example
```java
abstract class Vehicle {
    // Abstract method (no body)
    abstract void start();
}

class Car extends Vehicle {
    @Override
    void start() {
        System.out.println("Car starts with a key.");
    }
}

class Bike extends Vehicle {
    @Override
    void start() {
        System.out.println("Bike starts with a kick.");
    }
}
```

---

## 🔑 Difference Between Encapsulation and Abstraction

| Aspect              | Encapsulation                         | Abstraction                          |
|---------------------|---------------------------------------|--------------------------------------|
| **Focus**           | Hides the **data**                    | Hides the **implementation details** |
| **Achieved By**     | Using classes & access modifiers       | Using abstract classes & interfaces  |
| **Purpose**         | Protects the data and controls access | Provides a clear interface to users  |
| **Example**         | `private` fields with getters/setters | Abstract methods / Interfaces        |

---

## 🎯 Summary
- **Encapsulation** → Hides *data*.  
- **Abstraction** → Hides *implementation*.  

Both work together to increase **security**, **flexibility**, and **code reusability** in Object-Oriented Programming.
