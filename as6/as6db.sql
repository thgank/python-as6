PGDMP     0                    {            as6db    15.1    15.1     ?           0    0    ENCODING    ENCODING        SET client_encoding = 'UTF8';
                      false            ?           0    0 
   STDSTRINGS 
   STDSTRINGS     (   SET standard_conforming_strings = 'on';
                      false            ?           0    0 
   SEARCHPATH 
   SEARCHPATH     8   SELECT pg_catalog.set_config('search_path', '', false);
                      false            ?           1262    16899    as6db    DATABASE     }   CREATE DATABASE as6db WITH TEMPLATE = template0 ENCODING = 'UTF8' LOCALE_PROVIDER = libc LOCALE = 'Russian_Kazakhstan.1251';
    DROP DATABASE as6db;
                postgres    false            ?            1259    16919    user    TABLE     ?   CREATE TABLE public."user" (
    id integer NOT NULL,
    name character varying(50) NOT NULL,
    surname character varying(50) NOT NULL,
    mobile_number character varying(15) NOT NULL,
    email character varying(120) NOT NULL
);
    DROP TABLE public."user";
       public         heap    postgres    false            ?            1259    16918    user_id_seq    SEQUENCE     ?   CREATE SEQUENCE public.user_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;
 "   DROP SEQUENCE public.user_id_seq;
       public          postgres    false    215                        0    0    user_id_seq    SEQUENCE OWNED BY     =   ALTER SEQUENCE public.user_id_seq OWNED BY public."user".id;
          public          postgres    false    214            e           2604    16922    user id    DEFAULT     d   ALTER TABLE ONLY public."user" ALTER COLUMN id SET DEFAULT nextval('public.user_id_seq'::regclass);
 8   ALTER TABLE public."user" ALTER COLUMN id DROP DEFAULT;
       public          postgres    false    215    214    215            ?          0    16919    user 
   TABLE DATA           I   COPY public."user" (id, name, surname, mobile_number, email) FROM stdin;
    public          postgres    false    215   ?                  0    0    user_id_seq    SEQUENCE SET     9   SELECT pg_catalog.setval('public.user_id_seq', 9, true);
          public          postgres    false    214            g           2606    16926    user user_email_key 
   CONSTRAINT     Q   ALTER TABLE ONLY public."user"
    ADD CONSTRAINT user_email_key UNIQUE (email);
 ?   ALTER TABLE ONLY public."user" DROP CONSTRAINT user_email_key;
       public            postgres    false    215            i           2606    16924    user user_pkey 
   CONSTRAINT     N   ALTER TABLE ONLY public."user"
    ADD CONSTRAINT user_pkey PRIMARY KEY (id);
 :   ALTER TABLE ONLY public."user" DROP CONSTRAINT user_pkey;
       public            postgres    false    215            ?   {   x?%?;?0?z?0??,??\?Z?D?;??	N?Q???L1?k+??M??????ffס?[??Ĥ?k?#.UI?O??i??({	R???M????/?`v???`??:???????PD?3?&?     